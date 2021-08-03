import cv2
import numpy as np
import math

# Read the image
img = cv2.imread('pugnew.jpg',1)
height_ = 600
width_ = 600
img = cv2.resize(img,(width_,height_))
height, width = img.shape[:2]
cv2.imshow('Imagen Original', img)

shx = 0.09
shy = 0.09
A = np.array([[1,shy],
              [shx,1]])
B = np.array([0,0]) 

newImg = np.array(np.zeros(height_*width_*3).reshape(img.shape));
newImg = np.array(newImg, dtype=np.uint8)

for i in range(height):
    for j in range(width):
        position = np.array([i,j])
        new_position = np.dot(A,position) + B # [new_i,new_j]
        new_position = new_position.astype(int)

        if ((new_position[0] >= 0 and new_position[0] < height) and (new_position[1] >= 0 and new_position[1] < width)):
            newImg[new_position[0],new_position[1]] = img[i,j]

cv2.imshow('Imagen Shear', newImg)
 
filename = 'ShearPug2.jpg'
cv2.imwrite(filename, newImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
