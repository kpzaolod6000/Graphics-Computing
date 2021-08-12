import cv2
import numpy as np

# Read the image
img = cv2.imread('pug.jpg',1)
img = cv2.resize(img,(600,600))
rows, cols = img.shape[:2]
cv2.imshow('Imagen Original', img)

# # # Define the 3 pairs of corresponding points 

M = np.float32([[1,0,50], [0,1,50]])
print(M)
 
# # Apply the affine transformation using cv2.warpAffine()
imgResult = cv2.warpAffine(img, M, (cols,rps))
 
# # Display the image
# out = cv2.hconcat([img, dst]) // une las imagenes en una sola ventana
cv2.imshow('Result', imgResult)

filename = 'TraslacionPug.jpg'
cv2.imwrite(filename, imgResult)

cv2.waitKey(0)
cv2.destroyAllWindows()