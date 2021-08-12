import numpy as np

#EXPONENTIAL OPERATOR
#constant c yb 
def ExponentialOperator(img): 
    imgOut = img.copy()
    c = 20
    b = 1.01
    for i in range(len(imgOut)):
        for j in range(len(imgOut[0])):
            new_pixel = c * ((b**int(img[i][j])) - 1)
            imgOut[i][j] = np.uint8(new_pixel)
    return imgOut