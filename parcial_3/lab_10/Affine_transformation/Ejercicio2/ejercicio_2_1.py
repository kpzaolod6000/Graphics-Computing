import cv2
import numpy as np

# Read the image
img = cv2.imread('pug.jpg',1)
height_ = 600
width_ = 600
img = cv2.resize(img,(width_,height_))
height, width = img.shape[:2]
cv2.imshow('Imagen Original', img)

A = np.array([[1,0],
              [0,1]], dtype='int32')
B = np.array([-50,-50], dtype='int32') 



newImg = np.array(np.zeros(height_*width_*3).reshape(img.shape));
newImg = np.array(newImg, dtype=np.uint8)

# print(len(newImg))
# print(len(newImg[0]))
# print(newImg[0][0])

for i in range(height):
    for j in range(width):
        position = np.array([i,j], dtype='int32')
        new_position = np.dot(A,position) + B # [new_i,new_j]

        if ((new_position[0] >= 0 and new_position[0] < height) and (new_position[1] >= 0 and new_position[1] < width)):
            newImg[new_position[0],new_position[1]] = img[i,j]

cv2.imshow('Imagen Trasladada', newImg)
 

filename = 'TraslacionPug2.jpg'
cv2.imwrite(filename, newImg)


cv2.waitKey(0)
cv2.destroyAllWindows()