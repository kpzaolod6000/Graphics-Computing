import cv2
import numpy as np

def function(img):
    height,width,channels =img.shape

    emptyImage=np.zeros((600,600,channels),np.uint8)
    sh=600/height
    sw=600/width
    for i in range(600):
        value = 0
        for j in range(600-1):
            value = img[i,j] + img[i,j+1]
            value = int(value/2)
            
            y=int(j/sw)
            emptyImage[i,j]=img[x,y]
    return emptyImage
 
img=cv2.imread("dog.jpg")
zoom=function(img)
cv2.imshow("nearest neighbor",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)