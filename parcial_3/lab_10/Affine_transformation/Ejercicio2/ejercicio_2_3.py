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

angulo = 45
px= height/2
py= width/2 
A = np.array([[math.cos(angulo),math.sin(angulo)],
              [-math.sin(angulo),math.cos(angulo)]])
B = np.array([((1-math.cos(angulo)) * px) - (math.sin(angulo) * py),(math.sin(angulo) * px) + ((1-math.cos(angulo)) * py)]) 
print(A)
print(B)



newImg = np.array(np.zeros(height_*width_*3).reshape(img.shape));
newImg = np.array(newImg, dtype=np.uint8)
newImg2 = newImg.copy()
#Imagen rotada sin solve
for i in range(width):
    for j in range(height):
        position = np.array([i,j])
        new_position = np.dot(A,position) + B # [new_i,new_j]
        new_position = new_position.astype(int)
        x = new_position[0]
        y = new_position[1]
        if (( x>= 0 and x < height) and (y >= 0 and y < width)):
            newImg[new_position[0],new_position[1]] = img[i,j]
cv2.imshow('Imagen Rotada ', newImg)
filename = 'RotacionsPugERROR.jpg'
cv2.imwrite(filename, newImg)

#Imagen rotada con solve
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
            # newImg2[v, u] = img[y, x]
            newImg2[u, v] = img[x, y]

cv2.imshow('Imagen Rotada con solve', newImg2)
 
filename = 'RotacionPug2.jpg'
cv2.imwrite(filename, newImg2)

cv2.waitKey(0)
cv2.destroyAllWindows()