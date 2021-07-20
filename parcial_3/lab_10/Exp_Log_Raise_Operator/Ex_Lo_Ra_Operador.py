import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import math

imgReal = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
img = imgReal.copy()

#HISTOGRAMA
f, (ax1, ax2,ax3,ax4) = plt.subplots(4,1,figsize=(10, 15))# sharey=True, al introducir todas dimensiones de un histograma es compartido con los demas
ax1.hist(img.ravel(),256,[0,256])
ax1.set_title('Imagen Original')
# ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen Original',img)

#EXPONENTIAL OPERATOR
#constant c
c = 20
b = 1.01
for i in range(len(img)):
    for j in range(len(img[0])):
        new_pixel = c * ((b**int(img[i][j])) - 1)
        img[i][j] = np.uint8(new_pixel)

ax2.hist(img.ravel(),256,[0,256])
ax2.set_title('Imagen (Exponential Operator)')
# ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Exponential Operator)',img)

# filename = 'ExponentialPeaje.jpg'
# cv2.imwrite(filename, img)

#RAISE TO THE POWER OPERATOR
#constant c
img2 = imgReal.copy()
c = 0.05
r = 1.5
for i in range(len(img2)):
    for j in range(len(img2[0])):
        new_pixel = c * (int(img2[i][j])**r)
        img2[i][j] = np.uint8(new_pixel)

ax3.hist(img2.ravel(),256,[0,256])
ax3.set_title('Imagen (Raise to the power Operator)')
# ax3.set_xlabel('Intensidad')
ax3.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Raise to the power Operator)',img2)


# filename = 'RaisePeaje.jpg'
# cv2.imwrite(filename, img2)


#LOGARITMICO OPERATOR
#constant c
img3 = imgReal.copy()
c = 50
for i in range(len(img3)):
    for j in range(len(img3[0])):
        new_pixel = c * math.log10(1 + int(img3[i][j]))
        if (new_pixel > 255):
            new_pixel = 255
        img3[i][j] = np.uint8(new_pixel)


ax4.hist(img3.ravel(),256,[0,256])
ax4.set_title('Imagen (Logarithm Operator)')
# ax4.set_xlabel('Intensidad')
ax4.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Logarithm Operator)',img3)


# filename = 'LogaritmicPeaje.jpg'
# cv2.imwrite(filename, img3)
# plt.savefig('Histogramathreee.png')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()