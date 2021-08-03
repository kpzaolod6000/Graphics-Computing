import cv2
import numpy as np

imgReal1 = cv2.imread("ciudad.jpg",1) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1

imgReal2 = cv2.imread("leon.jpg",1) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(400,400))
img2 = imgReal2


cv2.imshow("Image Original 1", imgReal1)
cv2.imshow("Image Original 2", imgReal2)

B1, G1, R1 = cv2.split(img1)
B2, G2, R2 = cv2.split(img2)
B1, G1, R1 = B1.astype(int), G1.astype(int), R1.astype(int)
B2, G2, R2 = B2.astype(int), G2.astype(int), R2.astype(int)
Bresult,Gresult,Rresult = B1.copy(), G1.copy(), R1.copy()

print(B1.dtype)
# print(img2)
for i in range(len(B1)):
    for j in range(len(B1[0])):
        sum_B = B1[i,j]//2 + B2[i,j]//2
        if sum_B > 255 :
            Bresult[i,j] = 255
        else:
            Bresult[i,j] = sum_B
        
        sum_G = G1[i,j]//2 + G2[i,j]//2
        if sum_G > 255 :
            Gresult[i,j] = 255
        else:
            Gresult[i,j] = sum_G

        sum_R = R1[i,j]//2 + R2[i,j]//2
        if sum_R > 255 :
            Rresult[i,j] = 255
        else:
            Rresult[i,j] = sum_R

img_result = cv2.merge((Bresult,Gresult,Rresult))
img_result = np.array(img_result, dtype=np.uint8)
cv2.imshow('ResultadoLeonCiudad', img_result)
# filename = 'ResultadoLeonCiudad.jpg'
# cv2.imwrite(filename, img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()