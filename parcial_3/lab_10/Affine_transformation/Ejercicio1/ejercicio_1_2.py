import cv2
import numpy as np

# Read the image
img = cv2.imread('pug.jpg',1)
img = cv2.resize(img,(600,600))
rows, cols = img.shape[:2]
cv2.imshow('Imagen Original', img)

# Matriz M
M = np.float32([[2,0,0], [0,2,0]])
print(M)

# # Apply the affine transformation using cv2.warpAffine()
imgResult = cv2.warpAffine(img, M, (cols*2,rows*2))
 
cv2.imshow('Output', imgResult)

# filename = 'EscalarPug.jpg'
# cv2.imwrite(filename, imgResult)

cv2.waitKey(0)
cv2.destroyAllWindows()