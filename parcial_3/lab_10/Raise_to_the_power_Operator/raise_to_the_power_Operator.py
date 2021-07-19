import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import math

imgReal = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
img = imgReal

#HISTOGRAMA
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(15, 5))
ax1.hist(img.ravel(),256,[0,256])
ax1.set_title('Imagen Original')
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen Original',img)

#constant c
c = 0.05
r = 1.5
for i in range(len(img)):
    for j in range(len(img[0])):
        new_pixel = c * (int(img[i][j])**r)
        img[i][j] = np.uint8(new_pixel)

# am = int(img[0][0])
# print(am)
# print(type(am))

ax2.hist(img.ravel(),256,[0,256])
ax2.set_title('Imagen (Raise to the power Operator)')
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Raise to the power Operator)',img)


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()