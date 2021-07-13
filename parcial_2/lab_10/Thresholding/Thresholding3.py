import cv2
import numpy as np
from matplotlib import pyplot as plt

def getThresholding(img):
    modifiedImg = img
    print(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j] >= 180 and img[i][j] <= 210):#185 
                modifiedImg[i][j] = np.uint8(0)
            else:
                modifiedImg[i][j] = np.uint8(255)
    return modifiedImg

# read an image
imgColor = cv2.imread("campo.JPG",1) #8 bit por escala de grises
imgReal = cv2.imread("campo.JPG",cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
# imgReal = cv2.resize(imgReal,(600,600))
img = imgReal


#===================================================================================================
# tablas para los histogramas
#===================================================================================================
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(15, 5))
ax1.hist(img.ravel(),256,[0,256])
ax1.set_title('Imagen Original')
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')
ax1.set_ylim(0,8000)
# display the merged images
cv2.imshow('Image Original', imgColor)

#thresholding
#de acuerdo al histograma

u_img = getThresholding(img)
print(u_img)
ax2.hist(u_img.ravel(),256,[0,256])
ax2.set_title('Imagen (Contrast Stretching)')
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')
cv2.imshow('Imagen (Constrast Stretching)',u_img)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows() 

