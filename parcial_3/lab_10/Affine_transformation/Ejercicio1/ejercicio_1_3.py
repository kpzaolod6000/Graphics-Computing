import cv2
import numpy as np
import math

# Reading the img
img = cv2.imread('pug.jpg',1)
img = cv2.resize(img,(600,600))
# dividing height and width by 2 to get the center of the img
height, width = img.shape[:2]
# get the center coordinates of the img to create the 2D rotation matrix
# center = (width/2, height/2)

# using cv2.getRotationMatrix2D() to get the rotation matrix
# rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
# print(rotate_matrix)

# matriz
angulo = 45
px= 300.0
py= 300.0
M = np.float32([[math.cos(angulo),math.sin(angulo),((1-math.cos(angulo)) * px) - (math.sin(angulo) * py)], 
                [-math.sin(angulo),math.cos(angulo),(math.sin(angulo) * px) + ((1-math.cos(angulo)) * py)]])
print(M)
# rotate the img using cv2.warpAffine
rotated_img = cv2.warpAffine(src=img, M=M, dsize=(width, height))

cv2.imshow('imgen Original ', img)
cv2.imshow('imgen Rotada ', rotated_img)
# wait indefinitely, press any key on keyboard to exit


filename = 'RotacionPug.jpg'
cv2.imwrite(filename, rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()