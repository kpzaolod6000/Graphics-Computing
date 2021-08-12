import cv2
import numpy as np
from matplotlib import pyplot as plt

# widthImg = 500
# heightImg = 640

# cap = cv2.VideoCapture(0) #0 por defecto camera
# cap.set(3,1040)
# cap.set(4,480)
# cap.set(10,-150)
def PixelOperations(img,c,d):
    a = 0
    b = 255
    for row in range(len(img)):
        for pixel in range(len(img[row])):
            if(0<=img[row][pixel]  and img[row][pixel]  <= c):
                img[row][pixel] = (a/c)*img[row][pixel]
            elif(c<img[row][pixel] and img[row][pixel] <= d):
                img[row][pixel] = ((img[row][pixel] - c) * ((b-a)/(d-c)))+a
            else:
                 img[row][pixel] = ((img[row][pixel] - d) * ((255-b)/(255-d)))+b
    img = np.array(img, dtype=np.uint8)
    return img

def getThresholding(img,threshold):
    modifiedImg = img.copy()
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j] < threshold): 
                modifiedImg[i][j] = np.uint8(0)
            else:
                modifiedImg[i][j] = np.uint8(255)
    return modifiedImg


# def preProcesing(img):

#     # scale = 1
#     # delta = 0
#     # ddepth = cv2.CV_16S
#     imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  

#     imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)# para reducir el ruido
#     imgCanny = cv2.Canny(imgBlur,200,200) #era 200
#     # # SOBEL
#     # grad_x = cv2.Sobel(imgBlur, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
#     # # Gradient-Y
#     # # grad_y = cv.Scharr(gray,ddepth,0,1)
#     # grad_y = cv2.Sobel(imgBlur, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
#     # abs_grad_x = cv2.convertScaleAbs(grad_x)
#     # abs_grad_y = cv2.convertScaleAbs(grad_y)
#     # grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
#     # cv2.imshow("Sobel", grad)

#     # hist = cv2.calcHist([grad], [0], None, [256], [0, 256])
#     # plt.plot(hist, color='red' )

#     # imgThresold = getThresholding(grad,5)
#     # cv2.imshow("image Thresolding", imgThresold )
#     kernel = np.ones((5,5))
#     imgDial = cv2.dilate(imgCanny ,kernel,iterations = 2)
#     imgThres = cv2.erode(imgDial,kernel,iterations = 1)

   
#     cv2.imshow("image Canny",imgCanny)
#     cv2.imshow("image Dilate",imgDial)
#     cv2.imshow("image Thres", imgThres)
    
#     return imgThres

# def getContours(img):
#     biggest = np.array([])
#     maxArea = 0
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     # print(contours)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         # print(cnt)
#         # print(area)
#         if area > 5000:
#             cv2.drawContours(imgContour,cnt,-1,(0,255,0),3)
#             peri = cv2.arcLength(cnt,True)
#             approx =cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             if area > maxArea and len(approx) == 4:
                
#                 biggest = approx
#                 maxArea = area
#             # print(len(approx))
#             # objCor = len(approx)
#             # x,y,w,h = cv2.boundingRect(approx)
#     cv2.drawContours(imgContour,biggest,-1,(0,0,255),20)
#     return biggest

# def reorder(myPoints):
#     myPoints = myPoints.reshape((4,2))
#     myPointsNew = np.zeros((4,1,2),np.int32)
#     add = myPoints.sum(1)
#     # print("add",add)
#     myPointsNew[0] = myPoints[np.argmin(add)]
#     myPointsNew[3] = myPoints[np.argmax(add)]
    
#     diff = np.diff(myPoints,axis = 1)
#     myPointsNew[1] = myPoints[np.argmin(diff)]
#     myPointsNew[2] = myPoints[np.argmax(diff)]
#     # print("newPoints",myPointsNew)

#     return myPointsNew

# def getWarp(img,biggest):
#     if(len(biggest) == 0): return img
#     biggest = reorder(biggest)
#     image_cropping = np.float32(biggest)
#     windows_destiny = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])

#     matrix = cv2.getPerspectiveTransform(image_cropping,windows_destiny)
#     imgOutput = cv2.warpPerspective(img,matrix,(widthImg,heightImg))
#     # return imgOutput
#     #recortando
#     imgCropped =  imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
#     imgCropped = cv2.resize(imgCropped,(widthImg,heightImg))
#     return imgCropped
# global ImgResult
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img,(widthImg,heightImg))
#     imgThresold = preProcesing(img)
#     imgContour = img.copy()
#     biggest = getContours(imgThresold)
#     print(biggest)
#     imgWarped = getWarp(img,biggest)

#     cv2.imshow("image Result",imgWarped)
#     cv2.imshow("image Contour",imgContour)
#     # cv2.imshow("image Thresold",imgThresold)

    
#     #3########################################
#     # imgGray = cv2.cvtColor(imgWarped,cv2.COLOR_BGR2GRAY)
#     # hist = cv2.calcHist([imgGray], [0], None, [256], [0, 256])
#     # plt.plot(hist, color='red' )

#     cv2.imshow("Camera",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         ImgResult = imgWarped
#         cv2.imwrite("fondo.jpg", ImgResult)
#         break

imgGray = cv2.imread("result.jpg",cv2.IMREAD_GRAYSCALE)
# imgGray = cv2.cvtColor(ImgResult,cv2.COLOR_BGR2GRAY)  
#tablas para los histogramas
f, (ax1) = plt.subplots(1, 1, sharey=True,figsize=(15, 5))
ax1.hist(imgGray.ravel(),256,[0,256])
ax1.set_title("Imagen Gris")
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
# cv2.imshow("Imagen en Gris",imgGray)

imgThresold = getThresholding(imgGray,210)
cv2.imshow("image Thresolding", imgThresold )

#===================================================================================================
# DIVISION DE IMAGENES
#===================================================================================================

imgReal1 = cv2.imread("result.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1.copy()

imgReal2 = cv2.imread("fondo.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(400,400))
img2 = imgReal2.copy()

cv2.imshow("Image Original 1", imgReal1)
cv2.imshow("Image Original 2", imgReal2)

img1 = img1.astype(int)
img2 = img2.astype(int)
imgOperation = img1.copy()

for i in range(len(img1)):
    for j in range(len(img1[0])):
        result = (img1[i,j]/img2[i,j])*30
        # scala = (result-0)*(255-0)/(1-0) + 0
        imgOperation[i,j] = result
imgOperation = imgOperation.astype(np.uint8)
cv2.imshow("Resultado", imgOperation)

arrayImg = imgOperation.ravel()
sortArray = np.sort(arrayImg)
# print(sortArray)
# 0% y el 100 %
min_ = int(len(sortArray) * 0.0)
max_ = int(len(sortArray) * 1.0 -1)
c = sortArray[min_]
d = sortArray[max_]
img_Constrast = PixelOperations(imgOperation.astype(int),int(c),int(d))
cv2.imshow("Resultado constrast", img_Constrast)



plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows() 
