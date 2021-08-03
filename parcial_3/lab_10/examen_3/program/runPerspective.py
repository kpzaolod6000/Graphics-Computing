import cv2
import numpy as np
img = cv2.imread("hoja2.jpg")

img = cv2.resize(img,(400,500))

width,height = 400,500

image_cropping = np.float32([[51,438],[98,13],[288,480],[345,60]]) # los puntos estan al reves de la lista OJO
windows_destiny = np.float32([[0,0],[width,0],[0,height],[width,height]])


matrix = cv2.getPerspectiveTransform(image_cropping,windows_destiny)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("image",imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()