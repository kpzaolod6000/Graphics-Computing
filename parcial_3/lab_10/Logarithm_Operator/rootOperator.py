import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import math

imgReal = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
img = imgReal.copy()

#HISTOGRAMA
f, (ax1, ax2,ax3) = plt.subplots(1, 3, sharey=True,figsize=(15, 5))
ax1.hist(img.ravel(),256,[0,256])
ax1.set_title('Imagen Original')
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen Original',img)
#constant c
c = 100
for i in range(len(img)):
    for j in range(len(img[0])):
        new_pixel = c * math.log10(1 + int(img[i][j]))
        if (new_pixel > 255):
            new_pixel = 255
        img[i][j] = np.uint8(new_pixel)
#constant c


# am = int(img[0][0])
# print(am)
# print(type(am))

ax2.hist(img.ravel(),256,[0,256])
ax2.set_title('Imagen (Logarithm Operator)')
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Logarithm Operator)',img)


# filename = 'logaritmgalaxy.jpg'
# cv2.imwrite(filename, img)
#ROOT OPERATOR
img2 = imgReal.copy()
c = 20
for i in range(len(img2)):
    for j in range(len(img2[0])):
        new_pixel = c * math.sqrt(int(img2[i][j]))
        if (new_pixel > 255):
            new_pixel = 255
        img2[i][j] = np.uint8(new_pixel)

ax3.hist(img2.ravel(),256,[0,256])
ax3.set_title('Imagen (Root Operator)')
ax3.set_xlabel('Intensidad')
ax3.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Root Operator)',img2)


# plt.savefig('Histogramaroot.png')
# # Filename
# filename = 'rootgalaxy.jpg'
# cv2.imwrite(filename, img2)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()