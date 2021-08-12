import numpy as np

def EquationContrastStretching(img,c,d):
    a = 0
    b = 255
    imgOut = img.copy()
    for row in range(len(imgOut )):
        for pixel in range(len(imgOut[row])):
            if(0<=img[row][pixel]  and img[row][pixel]  <= c):
                imgOut[row][pixel] = (a/c)*img[row][pixel]
            elif(c<img[row][pixel] and img[row][pixel] <= d):
                imgOut[row][pixel] = ((img[row][pixel] - c) * ((b-a)/(d-c)))+a
            else:
                 imgOut[row][pixel] = ((img[row][pixel] - d) * ((255-b)/(255-d)))+b
    imgOut = np.array(imgOut , dtype=np.uint8)
    return imgOut 