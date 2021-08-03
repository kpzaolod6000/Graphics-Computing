import cv2
import numpy as np
import math

# Reading the img
img = cv2.imread('pugnew.jpg',1)
img = cv2.resize(img,(600,600))
# dividing height and width by 2 to get the center of the img
height, width = img.shape[:2]

# matriz
angulo = 45
px= height/2
py= width/2
M = np.float32([[math.cos(angulo),math.sin(angulo),((1-math.cos(angulo)) * px) - (math.sin(angulo) * py)], 
                [-math.sin(angulo),math.cos(angulo),(math.sin(angulo) * px) + ((1-math.cos(angulo)) * py)]])
print(M)

cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])

# compute the new bounding dimensions of the image
newWidth = int((height * sin) + (width * cos))
newHheight = int((height * cos) + (width * sin))

# adjust the rotation matrix to take into account translation
M[0, 2] += (newWidth / 2) - px
M[1, 2] += (newHheight / 2) - py
print(M)

# rotate the img using cv2.warpAffine
rotated_img = cv2.warpAffine(src=img, M=M, dsize=(nW, nH))
print(len(rotated_img))
print(len(rotated_img[0]))

# rotated = imutils. rotate_bound(imagen,  -33)
# cv2. imshow("Rotado sin recortar", rotado)
# cv2. waitKey(0)

cv2.imshow('imgen Original ', img)
cv2.imshow('imgen Rotada ', rotated_img)

filename = 'RotadaCorrectPug.jpg'
cv2.imwrite(filename, rotated_img)

# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
cv2.destroyAllWindows()