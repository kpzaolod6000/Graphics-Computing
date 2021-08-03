import cv2
import numpy as np
from matplotlib import pyplot as plt


def getThresholding(img,threshold):
    modifiedImg = img.copy()
    print(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j] < threshold): 
                modifiedImg[i][j] = np.uint8(0)
            else:
                modifiedImg[i][j] = np.uint8(255)
    return modifiedImg

imgReal1 = cv2.imread("texto1.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1

imgReal2 = cv2.imread("textoblanco.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
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

c = 110
for i in range(len(img1)):
    for j in range(len(img1[0])):
        rest = img1[i,j] - img2[i,j]
        imgResult[i,j] = rest + c
imgResult = imgResult.astype(np.uint8)
cv2.imshow("Resultado Sustraccion", imgResult)

# filename = 'Resultado_Sustraccion.jpg'
# cv2.imwrite(filename, imgResult)

f, (ax1) = plt.subplots(1, 1,figsize=(6, 6))
ax1.hist(imgResult.ravel(),256,[0,256])
ax1.set_title("Histograma")
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')

threshold = 90
imgThres = getThresholding(imgResult,threshold)
cv2.imshow("Resultado Thresolding", imgThres)

# filename = 'Resultado_Thresolding.jpg'
# cv2.imwrite(filename, imgThres)

# # Filename
# plt.savefig('HistogramaThresoldingSus.png')

# #HISTOGRAM EQUALIZATION

# histogramData = np.bincount(imgThres.flatten(),minlength=256)
# total_pixels = np.sum(histogramData)
# ##frecuencia
# Pn = histogramData/total_pixels
# #frecuencia acumulativa  
# Sn = np.cumsum(Pn)
# #floor
# Sn = np.floor(255*Sn).astype(np.uint8)
# # print(Sn)

# #matriz a lista
# img_list = list(imgThres.flatten())
# #cambiando los colores con los valores ecualizados
# img_update = [Sn[i] for i in img_list]
# img_update = np.reshape(np.asarray(img_update),imgThres.shape)
# cv2.imshow('Imagen (Histogram Equalization)',img_update)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()