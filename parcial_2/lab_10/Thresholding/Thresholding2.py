import cv2
import numpy as np
from matplotlib import pyplot as plt

def getThresholding(img):
    modifiedImg = img
    print(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j] > 175 and img[i][j] < 193): 
                modifiedImg[i][j] = np.uint8(0)
            else:
                modifiedImg[i][j] = np.uint8(255)
    return modifiedImg

# read an image
listImg = ["tejido1.JPG","tejido2.JPG"]
# threshold = [182,182]
for i in range(len(listImg)): 
    imgReal = cv2.imread(listImg[i],cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises

    # imgReal = cv2.resize(imgReal,(600,600))
    img = imgReal

    #tablas para los histogramas
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(15, 5))
    ax1.hist(img.ravel(),256,[0,256])
    title_ = "Imagen Original " + str(i+1)
    ax1.set_title(title_)
    ax1.set_xlabel('Intensidad')
    ax1.set_ylabel('Cantidad de pixeles')
    ax1.set_ylim(0,15000)
    # display the merged images
    cv2.imshow(title_, img)


    #thresholding
    #de acuerdo al histograma
    # img = getThresholding(img,threshold[i])
    img = getThresholding(img)
    print(img)
    ax2.hist(img.ravel(),256,[0,256])
    title_ = "Imagen (Contrast Stretching) " + str(i+1)
    ax1.set_title(title_)
    ax2.set_xlabel('Intensidad')
    ax2.set_ylabel('Cantidad de pixeles')
    cv2.imshow(title_,img)
    

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows() 

