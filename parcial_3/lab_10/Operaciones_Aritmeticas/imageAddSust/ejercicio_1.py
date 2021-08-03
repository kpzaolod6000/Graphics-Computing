import cv2
import numpy as np

imgReal1 = cv2.imread("image_1_1.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1

imgReal2 = cv2.imread("image_1_2.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(400,400))
img2 = imgReal2

cv2.imshow("Image Original 1", imgReal1)
cv2.imshow("Image Original 2", imgReal2)

img1 = img1.astype(int)
img2 = img2.astype(int)
imgResult = img1.copy()
# print(imgResult.dtype)
print(imgResult)
# imgResult = list(img1.flatten())
# imgResult = np.reshape(imgResult, (img1.shape[0], img1.shape[2]))

for i in range(len(img1)):
    for j in range(len(img1[0])):
        sum_ = img1[i,j]//2 + img2[i,j]//2
        if sum_ > 255 :
            imgResult[i,j] = 255
        else:
            imgResult[i,j] = sum_
imgResult = imgResult.astype(np.uint8)
cv2.imshow("Resultado", imgResult)
# filename = 'Resultado_Image1_2.jpg'
# cv2.imwrite(filename, imgResult)

cv2.waitKey(0)
cv2.destroyAllWindows()