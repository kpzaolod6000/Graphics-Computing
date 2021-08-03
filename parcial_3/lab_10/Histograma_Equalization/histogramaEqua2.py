import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys



imgReal = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
# imgReal = cv2.resize(imgReal,(600,600))
img = imgReal.copy()

#Recortar una imagen
imageOut = img[200:340,160:215]
# print(imageOut)
cv2.imshow('Imagen Real',imgReal)
histimg = cv2.resize(imageOut,(150,300))
# filename = 'CapillaRecortada.jpg'
# cv2.imwrite(filename, histimg)

#HISTOGRAMA
f, (ax1, ax2) = plt.subplots(1, 2,figsize=(15, 5))
ax1.hist(imageOut.ravel(),256,[0,256])
ax1.set_title('Imagen Original')
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen Recortada',histimg)

#HISTOGRAM EQUALIZATION

histogramData = np.bincount(imageOut.flatten(),minlength=256)
total_pixels = np.sum(histogramData)
##frecuencia
Pn = histogramData/total_pixels
#frecuencia acumulativa  
Sn = np.cumsum(Pn)
#floor
Sn = np.floor(255*Sn).astype(np.uint8)
# print(Sn)

#matriz a lista
img_list = list(img.flatten())
#cambiando los colores con los valores ecualizados
img_update = [Sn[i] for i in img_list]
img_update = np.reshape(np.asarray(img_update),img.shape)
print(img_update)


ax2.hist(img_update.ravel(),256,[0,256])
ax2.set_title('Imagen (Histogram Equalization)')
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Histogram Equalization)',img_update)
# # Filename
# plt.savefig('HistogramaRecortada.png')
# Filename
# filename = 'HistEquaRecortada.jpg'
# cv2.imwrite(filename, img_update)

           
# for intensity in histogramData:
#     print(int(intensity))

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()