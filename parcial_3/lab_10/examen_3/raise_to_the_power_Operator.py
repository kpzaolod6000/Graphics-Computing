import numpy as np

def raise_to_the_power_Operator(img):
    #constant c 
    c = 0.05
    r = 1.5
    imgOut = img.copy()
    for i in range(len(imgOut)):
        for j in range(len(imgOut[0])):
            new_pixel = c * (int(img[i][j])**r)
            imgOut[i][j] = np.uint8(new_pixel)
    return imgOut