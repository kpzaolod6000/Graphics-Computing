
import numpy as np

def ImagesSubtraction(imgOriginal1,imgOriginal2):
    imgInt1 = imgOriginal1.astype(int)
    imgInt2 = imgOriginal2.astype(int)
    imgResultSust = imgOriginal2.copy()

    c = 110
    for i in range(len(imgInt1)):
        for j in range(len(imgInt1[0])):
            rest = imgInt1[i,j] - imgInt2[i,j]
            scala = rest + c
            if(scala <0):
                imgResultSust[i,j] = 0
            else:
                if(scala > 255):
                    imgResultSust[i,j] = 255
                else:
                    imgResultSust[i,j] = scala
    imgResultSust = imgResultSust.astype(np.uint8)
    return imgResultSust