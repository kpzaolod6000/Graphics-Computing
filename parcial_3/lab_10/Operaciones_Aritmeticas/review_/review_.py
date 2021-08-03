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

def getThresholding2(img):
    modifiedImg = img.copy()
    # print(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j] >= 116 and img[i][j] <= 129):
                modifiedImg[i][j] = np.uint8(255) #200
            elif(img[i][j] < 130): 
                modifiedImg[i][j] = np.uint8(0)
            else:
                modifiedImg[i][j] = np.uint8(255)
    return modifiedImg

imgReal1 = cv2.imread("textReview1.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(600,400))
img1 = imgReal1.copy()

imgReal2 = cv2.imread("textReview2.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(600,400))
img2 = imgReal2.copy()

cv2.imshow("Image Original 1", imgReal1)
cv2.imshow("Image Original 2", imgReal2)

img1 = img1.astype(int)
img2 = img2.astype(int)
imgResultSust = img1.copy()
imgResultDiv = img1.copy()

# ============================================================================================
# SUSTRACION
# ============================================================================================
c = 130
for i in range(len(img1)):
    for j in range(len(img1[0])):
        rest = img1[i,j] - img2[i,j]
        if(rest <0):
            imgResultSust[i,j] = 0
        else:
            scala = rest + c
            if(scala >255):    
                imgResultSust[i,j] = 0
            else:
                imgResultSust[i,j] = rest + c
        
imgResultSust = imgResultSust.astype(np.uint8)
cv2.imshow("Resultado Sustraccion", imgResultSust)
# filename = 'ReviewSustraccion.jpg'
# cv2.imwrite(filename, imgResultSust)

f, (ax1,ax2) = plt.subplots(1, 2,figsize=(15, 5))
ax1.hist(imgResultSust.ravel(),256,[0,256])
ax1.set_title("Histograma Sustraccion")
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Cantidad de pixeles')

threshold = 1
imgSustThres = getThresholding(imgResultSust,threshold)
cv2.imshow("Thresolding Sustraccion", imgSustThres)
# filename = 'ReviewThresoldingSust.jpg'
# cv2.imwrite(filename, imgSustThres)

# ============================================================================================
# DIVISION
# ============================================================================================

for i in range(len(img1)):
    for j in range(len(img1[0])):
        result = (img1[i,j]/img2[i,j])
        # print(result)
        scala = (result-0)*(255-0)/(2-0) + 0
        imgResultDiv[i,j] = int(scala)
imgResultDiv = imgResultDiv.astype(np.uint8)
cv2.imshow("Resultado Division", imgResultDiv)
# filename = 'ReviewDivision.jpg'
# cv2.imwrite(filename, imgResultDiv)

ax2.hist(imgResultDiv.ravel(),256,[0,256])
ax2.set_title("Histograma Division")
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Cantidad de pixeles')

imgDivThres = getThresholding2(imgResultDiv)
cv2.imshow("Thresolding Division", imgDivThres)
# filename = 'ReviewThresoldingDiv.jpg'
# cv2.imwrite(filename, imgDivThres)

# Filename
plt.savefig('HistogramaRview.png')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()