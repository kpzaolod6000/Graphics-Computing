import numpy as np
import math


# LOGARITHM OPERATOR

def  LogarithmOperator(img): 
    #constant c
    imgOut = img.copy()
    c = 100
    for i in range(len(imgOut)):
        for j in range(len(imgOut[0])):
            new_pixel = c * math.log10(1 + int(img[i][j]))
            if (new_pixel > 255):
                new_pixel = 255
            imgOut[i][j] = np.uint8(new_pixel)
    return imgOut