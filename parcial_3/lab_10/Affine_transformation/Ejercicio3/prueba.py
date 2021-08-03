import cv2
import numpy as np
import math

matrix = np.array([ [56,23,15],
                    [65,32,78],
                    [12,45,62]])

newImg = np.array(np.zeros((matrix.shape[0]+1) * (matrix.shape[1]+1)).reshape((matrix.shape[0]+1,matrix.shape[1]+1)));
newImg = np.array(newImg, dtype=np.uint8)
print(newImg)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(i == len(matrix) - 1):
            # newImg[i,j] = matrix[i,j]
            # if j == len(matrix[i]) - 1:
            #     newImg[i,j] = matrix[i,j]
            #     newImg[i+1,j] = matrix[i,j]
            # else:
            newImg[i+1,j] = matrix[i,j]
        else:
            if j == len(matrix[i]) - 1:
                newImg[i,j] = matrix[i,j]
                newImg[i,j+1] = matrix[i,j]
                newImg[i+1,j] = matrix[i+1,j]
                
            else:
                newImg[i,j] = matrix[i,j]
                newImg[i,j+1] = matrix[i,j+1]
                newImg[i+1,j] = matrix[i+1,j]
                
                
print(newImg)
        # print(matrix[i][j])

