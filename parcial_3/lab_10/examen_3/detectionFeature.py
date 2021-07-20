
import numpy as np
import cv2
from matplotlib import pyplot as plt
 
img = cv2.imread('hoja4.jpg')
img = cv2.resize(img,(400,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 4, 0.15 , 10)

# El resultado devuelto es una matriz de [[311., 250.]] dos niveles de paréntesis.
corners = np.int0(corners)
print(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, 255, -1)
 
# plt.imshow(img), plt.title('Dstination'), plt.axis('off')
# plt.show()
cv2.imshow("result",img),

# if cv.waitKey(0) & 0xff == 27:
#     cv.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()