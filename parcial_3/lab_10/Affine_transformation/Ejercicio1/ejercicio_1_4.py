import cv2
import numpy as np
import math

# Reading the img
img = cv2.imread('pug.jpg',1)
img = cv2.resize(img,(600,600))
# dividing height and width by 2 to get the center of the img
height, width = img.shape[:2]

shx = 0.05
shy = 0.05
M = np.float32([[1,shy,0], 
                [shx,1,0]])
print(M)

# # Apply the affine transformation using cv2.warpAffine()
imgShear = cv2.warpAffine(img, M, (width,height))
 
cv2.imshow('Imagen Original ', img)
cv2.imshow('Imagen Shear',imgShear)

filename = 'ShearPug.jpg'
cv2.imwrite(filename, imgShear)
# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
cv2.destroyAllWindows()