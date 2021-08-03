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

A = np.array([[2.0,0.0],
              [0.0,2.0]])
B = np.array([0.0,0.0]) 

# Imagen escalada sin solve
newImg = np.array(np.zeros((height_*2)*(width_*2)*3).reshape((img.shape[0]*2,img.shape[1]*2,img.shape[2])));
newImg = np.array(newImg, dtype=np.uint8)

for i in range(height):
    for j in range(width):
        position = np.array([i,j])
        new_position = np.dot(A,position) + B # [new_i,new_j]
        new_position = new_position.astype(int)
        if ((new_position[0] >= 0 and new_position[0] < height*2) and (new_position[1] >= 0 and new_position[1] < width*2)):
            newImg[new_position[0],new_position[1]] = img[i,j]
cv2.imshow('Imagen Escalada ', newImg)
filename = 'EscalacionPugERROR.jpg'
cv2.imwrite(filename, newImg)

# Imagen escalada con solve
newImg2 = np.array(np.zeros((height_)*(width_)*3).reshape((img.shape)));
newImg2 = np.array(newImg2, dtype=np.uint8)

X = np.array([0,0])
for u in range(width):
    for v in range(height):
        Y = np.array([u,v]) - B
        solve_= cv2.solve(A, Y, X)
        X = solve_[1]
        X = X.astype(int)
        x = X[0]
        y = X[1]
        if ((x >= 0 and x < width) and (y>= 0 and y < height)):
            # print(x)
            # print(y)
            newImg2[v, u] = img[y, x]


cv2.imshow('Imagen Escalada con solve', newImg2)
 
filename = 'EscalacionPug2.jpg'
cv2.imwrite(filename, newImg2)


cv2.waitKey(0)
cv2.destroyAllWindows()