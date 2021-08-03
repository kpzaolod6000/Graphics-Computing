import cv2
import numpy as np
import math

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

imgReal1 = cv2.imread("tools1.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1

imgReal2 = cv2.imread("tools2.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(400,400))
img2 = imgReal2

cv2.imshow("Image Original 1", imgReal1)
cv2.imshow("Image Original 2", imgReal2)

img1 = img1.astype(int)
img2 = img2.astype(int)
imgResult = img1.copy()

for i in range(len(img1)):
    for j in range(len(img1[0])):
        result = (img2[i,j]/img1[i,j])*30
        # scala = (result-0)*(255-0)/(1-0) + 0
        imgResult[i,j] = result
imgResult = imgResult.astype(np.uint8)
cv2.imshow("Resultado", imgResult)

# filename = "Resultado_Division_Tools.jpg"
# cv2.imwrite(filename, imgResult)

arrayImg = imgResult.ravel()
sortArray = np.sort(arrayImg)
# print(sortArray)
# 0% y el 100 %
min_ = int(len(sortArray) * 0.0)
max_ = int(len(sortArray) * 1.0 -1)
c = sortArray[min_]
d = sortArray[max_]
img_Constrast = PixelOperations(imgResult.astype(int),int(c),int(d))
cv2.imshow("Resultado constrast", img_Constrast)

# filename = "Resultado_constrast_Tools.jpg"
# cv2.imwrite(filename, img_Constrast)

cv2.waitKey(0)
cv2.destroyAllWindows()