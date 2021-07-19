import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import math

def test_():
    histogramData = [790,1023,850,656,329,245,122,81]
    totalPixel = 4096
    Pn = np.zeros(8)
    for k in range(len(Pn)):
        Pn[k] = histogramData[k]/totalPixel

    Sn = np.zeros((8,), dtype=int)

    for i in range(len(Sn)):
        L = 8
        sumPn = 0
        for j in range(i+1):
            sumPn += Pn[j]
        Sn[i] = math.floor((L-1)*sumPn)
    return Sn 

def HistogramEqualization(histogramData,row,column):
    totalPixel = row*column
    
    Pn = np.zeros(len(histogramData))
    for k in range(len(Pn)):
        Pn[k] = int(histogramData[k])/totalPixel

    Sn = np.zeros((len(histogramData),), dtype=int)

    for i in range(len(Sn)):
        L = 256
        sumPn = 0
        for j in range(i+1):
            sumPn += Pn[j]
        Sn[i] = math.floor((L-1)*sumPn)
    return Sn 

imgReal = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
# imgReal = cv2.resize(imgReal,(600,600))
img = imgReal

#Recortar una imagen
# imageOut = img[60:220,280:480]
# cv2.imshow('Imagen recortado',imageOut)

# print(img.shape)

#HISTOGRAMA
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(15, 5))
hist_mask = ax1.hist(img.ravel(),256,[0,256])
ax1.set_title('Imagen Original')
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen Original',img)

histogramData = hist_mask[0]


# print(test_())
# print(histogramData)
Sn = HistogramEqualization(histogramData,img.shape[0],img.shape[1])
# print(Sn)
for i in range(len(img)):
    for j in range(len(img[i])):
        img[i][j] = np.uint8( Sn[img[i][j]] )#a la posicion del color agrega un nuevo color modificado

ax2.hist(img.ravel(),256,[0,256])
ax2.set_title('Imagen (Histogram Equalization)')
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Histogram Equalization)',img)
# # Filename
# plt.savefig('Histograma3.png')
# # Filename
# filename = 'HistEquaCapilla.jpg'
# cv2.imwrite(filename, img)

           
# for intensity in histogramData:
#     print(int(intensity))

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()