import cv2
import numpy as np
from matplotlib import pyplot as plt
import mapper
import Thresholding as Ts
import HistogramEqualization as He
import ExponentialOperator as Oe
import LogarithmOperator as Ol
import raise_to_the_power_Operator as ORp
import ContrastStretching as Cs
import Subtraction as Subt
import Division as Div

widthImg = 500
heightImg = 640

cap = cv2.VideoCapture(0) #0 por defecto camera
cap.set(3,1040*2) # altura
cap.set(4,480*2) # ancho
cap.set(10,150) #brillo

#===============================================================================================
# aplicando OPERADORES MORFOLOGICOS
#===============================================================================================
def MorphologyOperator(img):

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    
    #Aplicando filtrado gaussiano para suavisar la imagen
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    #Aplicando algoritmo de deteccion de bordes canny
    imgCanny = cv2.Canny(imgBlur,200,200) 
    
    #Aplicando operador Closing
    kernel = np.ones((5,5)) # Kernel de unos de tamaño 5X5
    imgDilate = cv2.dilate(imgCanny ,kernel,iterations = 2)
    imgErode = cv2.erode(imgDilate,kernel,iterations = 1)

   
    # cv2.imshow("image Canny",imgCanny)
    # cv2.imshow("image Dilate",imgDilate)
    # cv2.imshow("image Erode", imgErode)
    
    return imgErode

#===============================================================================================
# aplicando Connected Components: Metodo FindContours
#===============================================================================================

def ConnectedComponents(img,setImgContour):
    findContour = np.array([])
    contours, _ = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)

    #el bucle extrae los contornos de los límites de la página
    for c in contours:
        perimeter=cv2.arcLength(c,True)#longitud de cada contorno
        approx=cv2.approxPolyDP(c,0.02*perimeter,True)#retorna los puntos de los puntos de esquina

        if len(approx)==4:
            color_ = (150,150,150)
            cv2.drawContours(setImgContour, [approx], 0, (250,94,48),3)
            puntos = approx.reshape((4,2))
            cv2.circle(setImgContour, tuple(puntos[0]), 15, color_, 5)
            cv2.circle(setImgContour, tuple(puntos[1]), 15, color_, 5)
            cv2.circle(setImgContour, tuple(puntos[2]), 15, color_, 5)
            cv2.circle(setImgContour, tuple(puntos[3]), 15, color_, 5)
            findContour=approx
            break
    
    # cv2.drawContours(imgContour,findContour,-1,(0,255,0),20)
    return findContour

#===============================================================================================
# aplicando Transformacion de Perspectiva 
#===============================================================================================


def PerspectiveTransformation(img,Contour):
    if(len(Contour) == 0): return img
    #Aplicando ordenamiento a los puntos
    ptsContour = mapper.mapp(Contour)

    #Deformando la imagen real a la ventana de la salida deseada
    pts1 = np.float32(ptsContour)
    pts2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]]) # windows destiny

    M = cv2.getPerspectiveTransform(pts1,pts2)
    imgResult = cv2.warpPerspective(img,M,(widthImg,heightImg))
    # M = cv2.getAffineTransform(pts1,pts2)
    # imgResult = cv2.warpAffine(img,M,(widthImg,heightImg))
    
    #recortando errores
    imgCropped =  imgResult[20:imgResult.shape[0]-20,20:imgResult.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(widthImg,heightImg))
    return imgCropped

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    for i in range(len(im_list)):
        im_list[i] = cv2.resize(im_list[i],(600,600))
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

    
def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


global ImgResult

while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgEdge = MorphologyOperator(img)

    imgContour = img.copy()
    Contour = ConnectedComponents(imgEdge,imgContour)
    # print(biggest)
    imgPersp = PerspectiveTransformation(img,Contour)

    #Mostrando deteccion de bordes
    cv2.imshow("Imagen con Bordes",imgEdge)
    #Mostrando contornos
    cv2.imshow("Imagen con Contorno",imgContour)
    #Mostrando Resultados Scanner
    cv2.imshow("Imagen Resultado",imgPersp)
    #Camera Real
    # cv2.imshow("Camera Principal",img)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        ImgResult = imgPersp
        break
    elif key == ord('z'):
        cv2.imwrite("front.jpg", imgPersp)
    elif key == ord('x'):
        cv2.imwrite("back.jpg", imgPersp)

#===============================================================================================
# Lectura del imagenes escaneadas
#===============================================================================================
img1 = cv2.imread("front.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Imagen Original 1", img1)

img2 = cv2.imread("back.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Imagen Original 2", img2)

#===============================================================================================
# Aplicando Thresholding
#===============================================================================================
#tablas para los histogramas
# f, (ax1) = plt.subplots(1, 1, sharey=True,figsize=(15, 5))
# ax1.hist(img1.ravel(),256,[0,256])
# ax1.set_title("Histograma")
# ax1.set_xlabel('Intensidad')
# ax1.set_ylabel('Cantidad de pixeles')

imgThresold = Ts.getThresholding(img1,210)#210
cv2.imshow("Imagen Thresolding", imgThresold )

f, (ax1) = plt.subplots(1, 1, sharey=True,figsize=(15, 5))
ax1.hist(imgThresold.ravel(),256,[0,256])
ax1.set_title("Histograma")
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
#===============================================================================================
# Aplicando Histogram Equalization
#===============================================================================================
#Recortar una imagen
imageOut = img1[450:550,300:450]
imgEqualized = He.getHistogramEqua(img1,imageOut)
# cv2.imshow("Imagen Equalizada", imgEqualized)

# cv2.imshow("Imagen recortada", imageOut)

#===============================================================================================
# Aplicando Exponential Operator 
#===============================================================================================
imgExpn = Oe.ExponentialOperator(img1)
# cv2.imshow("Operador Exponencial", imgExpn)


#===============================================================================================
# Aplicando Logarithm Operator (opcional)
#aca se aplico de exponential a logaritmico 
#===============================================================================================
imgLog = Ol.LogarithmOperator(imgExpn)
# cv2.imshow("Operador Logarithm", imgLog)

#===============================================================================================
# Aplicando Raise to the power Operator
#
#===============================================================================================
imgRpower = ORp.raise_to_the_power_Operator(img1)
# cv2.imshow("Operador Raise to the Power", imgRpower)

#===============================================================================================
# Aplicando Constrast Stretching
#===============================================================================================
# por escala de grises en 8 bit entonces
arrayImg = img1.ravel()
sortArray = np.sort(arrayImg)
# 0% y el 100 %
min_ = int(len(sortArray) * 0.0)
max_ = int((len(sortArray) * 1.0) - 1)
c = sortArray[min_]
d = sortArray[max_]
imgConstrast = Cs.EquationContrastStretching(img1.astype(int),int(c),int(d))

# cv2.imshow("Constrast Stretching", imgConstrast)


#===============================================================================================
# Aplicando Sustraccion de imagenes
#===============================================================================================
imgResultSust = Subt.ImagesSubtraction(img1,img2)
# cv2.imshow("Resultado Sustraccion", imgResultSust)


threshold = 90
imgResultSust = Ts.getThresholding(imgResultSust,threshold)
# cv2.imshow("Sustraccion Thresolding", imgResultSust)

#===============================================================================================
# Aplicando Division de imagenes
#===============================================================================================
imgResultDiv = Div.ImagesDivision(img1,img2)
cv2.imshow("Resultado Division", imgResultDiv)

# por escala de grises en 8 bit entonces
arrayImg = imgResultDiv.ravel()
sortArray = np.sort(arrayImg)
# 0% y el 100 %
min_ = int(len(sortArray) * 0.0)
max_ = int((len(sortArray) * 1.0) - 1)
c = sortArray[min_]
d = sortArray[max_]
imgConstrast = Cs.EquationContrastStretching(imgResultDiv.astype(int),int(c),int(d))

# cv2.imshow("Division Constrast Stretching", imgConstrast)

threshold = 164
imgResultDiv = Ts.getThresholding(imgConstrast,threshold)
# cv2.imshow("Division Thresolding", imgResultDiv)



# im1_s = cv2.resize(im1, dsize=(0, 0), fx=0.5, fy=0.5)
# im_tile = concat_tile([[, ,,]])
# cv2.imwrite('data/dst/opencv_concat_tile.jpg', im_tile)



plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()