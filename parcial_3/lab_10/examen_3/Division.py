
import numpy as np

def ImagesDivision(imgOriginal1,imgOriginal2):
    imgInt1 = imgOriginal1.astype(int)
    imgInt2 = imgOriginal2.astype(int)
    imgResultDiv = imgOriginal2.copy()

    for i in range(len(imgInt1)):
        for j in range(len(imgInt1[0])):
            result = (imgInt1[i,j]/imgInt2[i,j])
            # print(result)
            scala = (result-0)*(255-0)/(2-0) + 0
            # imgResultDiv[i,j] = result * 100
            imgResultDiv[i,j] = scala
    imgResultDiv = imgResultDiv.astype(np.uint8)
    return imgResultDiv