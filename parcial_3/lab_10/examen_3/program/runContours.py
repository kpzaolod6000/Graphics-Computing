import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # print(contours)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(0,0,255),1)# -1 indice de contorno para dibujar todos
            peri = cv2.arcLength(cnt,True)#longitud de cada contorno
            approx =cv2.approxPolyDP(cnt,0.02*peri,True) #retorna los puntos de los puntos de esquina
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objCor == 3 : objectType = "Triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.95 and aspRatio<1.05:objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor >4: objectType = "Circle"
            else: objectType = "None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)#x y y puntos x+w ancho, y+h altura
            cv2.putText(imgContour ,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)

        #drawContours dibuja los contornos de los dibujos


path = "geometry.jpg"
img = cv2.imread(path)
imgContour = img.copy()

imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGRAY,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
cv2.imshow("image",img)
cv2.imshow("gray",imgGRAY)
cv2.imshow("blur",imgBlur)
cv2.imshow("canny",imgCanny)
cv2.imshow("imgCONTOURS",imgContour)
cv2.waitKey(0)  
cv2.destroyAllWindows()