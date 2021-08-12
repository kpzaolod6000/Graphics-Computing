import numpy as np
def getThresholding(img,threshold):
    modifiedImg = img.copy()
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j] < threshold): 
                modifiedImg[i][j] = np.uint8(0)
            else:
                modifiedImg[i][j] = np.uint8(255)
    return modifiedImg