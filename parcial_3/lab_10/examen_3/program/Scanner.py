import cv2
import numpy as np

widthImg = 500
heightImg = 640

cap = cv2.VideoCapture(0) #0 por defecto camera
cap.set(3,1040)
cap.set(4,480)
cap.set(10,150)

def preProcesing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations = 2)
    imgThres = cv2.erode(imgDial,kernel,iterations = 1)
   
    # cv2.imshow("image Dial",imgDial)
    
    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # print(contours)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(cnt)
        # print(area)
        if area > 5000:
            cv2.drawContours(imgContour,cnt,-1,(0,255,0),3)
            peri = cv2.arcLength(cnt,True)
            approx =cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            if area > maxArea and len(approx) == 4:
                
                biggest = approx
                maxArea = area
            # print(len(approx))
            # objCor = len(approx)
            # x,y,w,h = cv2.boundingRect(approx)
    cv2.drawContours(imgContour,biggest,-1,(0,0,255),20)
    return biggest

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    # print("add",add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    
    diff = np.diff(myPoints,axis = 1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    # print("newPoints",myPointsNew)

    return myPointsNew

def getWarp(img,biggest):
    if(len(biggest) == 0): return img
    biggest = reorder(biggest)
    image_cropping = np.float32(biggest)
    windows_destiny = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])

    matrix = cv2.getPerspectiveTransform(image_cropping,windows_destiny)
    imgOutput = cv2.warpPerspective(img,matrix,(widthImg,heightImg))
    # return imgOutput
    #recortando
    imgCropped =  imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(widthImg,heightImg))
    return imgCropped


while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgThresold = preProcesing(img)
    imgContour = img.copy()
    biggest = getContours(imgThresold)
    print(biggest)
    imgWarped = getWarp(img,biggest)

    cv2.imshow("image Result",imgWarped)
    cv2.imshow("image Contour",imgContour)
    cv2.imshow("image Thresold",imgThresold)
    

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break