import cv2
import numpy as np
from matplotlib import pyplot as plt

def EquationContrastStretching(pixel,a,b,c,d):
    g = ((pixel - c) * ((b-a)/(d-c)))+a
    return g
def PixelOperations(img,c,d):
    a = 0
    b = 255
    for row in range(len(img)):
        for pixel in range(len(img[row])):
            img[row][pixel] = EquationContrastStretching(img[row][pixel],a,b,c,d)
    img = np.array(img, dtype=np.uint8)
    return img


imgReal1 = cv2.imread("tools_1.jpg",  cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1

imgReal2 = cv2.imread("tools_2.jpg",  cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(400,400))
img2 = imgReal2

cv2.imshow("Image Original 1", imgReal1)
cv2.imshow("Image Original 2", imgReal2)

img1 = img1.astype(int)
img2 = img2.astype(int)
imgResult = img1.copy()
# print(imgResult.dtype)
print(imgResult)

add = 100
for i in range(len(img1)):
    for j in range(len(img1[0])):
        rest = abs(img1[i,j] - img2[i,j])
        imgResult[i,j] = rest
imgResult = imgResult.astype(np.uint8)
cv2.imshow("Resultado Sustraccion tools", imgResult)

filename = 'Resultado_Sustraccion_tools.jpg'
cv2.imwrite(filename, imgResult)

arrayImg = imgResult.ravel()
sortArray = np.sort(arrayImg)

# 0% y el 100 %
min_ = int(len(sortArray) * 0.0)
max_ = int(len(sortArray) * 1.0 - 1)
c = sortArray[min_]
d = sortArray[max_]
# print(c)
# print(d)
# print(imgResult.min())
# print(imgResult.max())
# imgContrast = PixelOperations(imgResult.astype(int),int(c),int(d))
# cv2.imshow("Resultado contrast", imgContrast)


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()