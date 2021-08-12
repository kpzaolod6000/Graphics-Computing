import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')
rows,cols,ch = img.shape


def getAffineTransform(pts1, pts2):
    p = []
    for x,y in pts1:
        p.append((x,y,1))
    # print(p)
    # print(pts2)
    # print(np.linalg.solve(p, pts2))
    return np.linalg.solve(p, pts2).T

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[50,50],[200,50],[200,250]])

M = getAffineTransform(pts1,pts2)
print(M)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.savefig('ImagenAffineTransform2.png')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()