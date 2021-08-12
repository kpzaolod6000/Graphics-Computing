import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[50,50],[200,50],[200,250]])

# print(pts1)
# print(pts2)
M = cv2.getAffineTransform(pts1,pts2)
print(M)

dst = cv2.warpAffine(img,M,(cols,rows))
# print(rows)
# print(len(dst))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.savefig('ImagenAffineTransform.png')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()