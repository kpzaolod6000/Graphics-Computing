
import numpy as np
import cv2 as cv
filename = 'chess.png'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
#result se usa para marcar esquinas, no es importante
dst = cv.dilate(dst,None)
 # Umbral del mejor valor, puede variar de una imagen a otra.
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()