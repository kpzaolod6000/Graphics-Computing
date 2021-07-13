  
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

imgReal = cv2.imread("dama.JPG", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal = cv2.resize(imgReal,(600,600))
img = imgReal

#tablas para los histogramas
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(15, 5))

for i in range(20):
    for j in range(20):
        img[i][j] = 0
ax1.hist(img.ravel(),256,[0,256])
ax1.set_title('Imagen Original')
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen real',img)

# por escala de grises en 8 bit entonces
arrayImg = img.ravel()
sortArray = np.sort(arrayImg)
print(sortArray)
# 5% y el 95 %
# min_ = 0
# max_ = int(len(sortArray) - 1)

min_ = int(len(sortArray) * 0.0015)
max_ = int(len(sortArray) * 0.9995)
c = sortArray[min_]
d = sortArray[max_]
print(len(sortArray))
print(min_)
print(c)
print(max_)
print(d)
img = PixelOperations(img.astype(int),int(c),int(d))

ax2.hist(img.ravel(),256,[0,256])
ax2.set_title('Imagen (Contrast Stretching)')
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Constrast Stretching)',img)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()