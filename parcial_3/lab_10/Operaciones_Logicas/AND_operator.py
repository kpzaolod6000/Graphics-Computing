import cv2
import numpy as np
from matplotlib import pyplot as plt


def getThresholding(img,threshold):
    modifiedImg = img.copy()
    # print(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j] < threshold): 
                modifiedImg[i][j] = np.uint8(0)
            else:
                modifiedImg[i][j] = np.uint8(255)
    return modifiedImg

imgReal1 = cv2.imread("pernos1.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1.copy()

imgReal2 = cv2.imread("pernos2.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(400,400))
img2 = imgReal2.copy()

img1 = 255-img1
img2 = 255-img2

# for i in range(len(img1)):
#     for j in range(len(img1[0])):
#         notImg1 =  255 - img1[i,j]
#         img1[i,j] = notImg1
#         notImg2 =  255 - img2[i,j]
#         img2[i,j] = notImg2

# filename = 'Inversionpernos1.jpg'
# cv2.imwrite(filename, img1)
# filename = 'Inversionpernos2.jpg'
# cv2.imwrite(filename, img2)

        
cv2.imshow("Image Original 1", img1)
cv2.imshow("Image Original 2", img2)

f, (ax1,ax2) = plt.subplots(1, 2,figsize=(15, 5))
ax1.hist(img1.ravel(),256,[0,256])
ax1.set_title("Histograma IMG1")
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
ax2.hist(img2.ravel(),256,[0,256])
ax2.set_title("Histograma IMG2")
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')


threshold = 98
imgThres1 = getThresholding(img1,threshold)
cv2.imshow("Resultado Thresolding de la IMG1", imgThres1)
# filename = 'ResultadoThresoldingPernos1.jpg'
# cv2.imwrite(filename, imgThres1)

imgThres2 = getThresholding(img2,threshold)
cv2.imshow("Resultado Thresolding de la IMG2", imgThres2)
# filename = 'ResultadoThresoldingPernos2.jpg'
# cv2.imwrite(filename, imgThres2)

# =============================================================================================
# OPERADOR AND
# =============================================================================================

imgResult = imgThres1.copy()

for i in range(len(imgThres1)):
    for j in range(len(imgThres1[0])):
        result = imgThres1[i,j] & imgThres2[i,j]
        imgResult[i,j] = result 
cv2.imshow("Resultado Operador AND", imgResult)

# filename = 'ResultadoOperadorAND.jpg'
# cv2.imwrite(filename, imgResult)

# Filename
# plt.savefig('HistogramaThresoldPernos.png')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()