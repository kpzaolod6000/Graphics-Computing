import cv2
import numpy as np
import random

img=cv2.imread("pugnew.jpg",0)

height = 100
width = 100
imgReal1 = cv2.resize(img,(width,height))
filename = 'pugOriginal.jpg'
cv2.imwrite(filename, imgReal1)


height,width =imgReal1.shape
# height,width,channels =imgReal1.shape
newTam=6
# emptyImage=np.zeros((width*newTam,height*newTam,channels),np.uint8)
 
emptyImageReplication=np.zeros((width*newTam,height*newTam),np.uint8)
 
cv2.imshow("Imagen Original",img)

# ESCALACION CON REPLICATION
i_run = 0
j_run = 0

for i in range(width):
    for j in range(height):
        for x in range(newTam):
            for y in range(newTam):
                if(j == 0 or j == height-1):
                    emptyImageReplication[i_run+x,j_run+y] = imgReal1[i,j]
                else:
                    emptyImageReplication[i_run+x,j_run+y] = random.choice([imgReal1[i,j],imgReal1[i,j+1]])
        j_run += newTam
    j_run = 0
    i_run += newTam

cv2.imshow("Resultado Replicacion",emptyImageReplication)
filename = 'ResultadoReplicacion.jpg'
cv2.imwrite(filename, emptyImageReplication)


# ESCALACION CON INTERPOLATION
i_run = 0
j_run = 0

emptyImageInterpolation=np.zeros((width*newTam,height*newTam),np.uint8)
for i in range(width):
    for j in range(height):
        for x in range(newTam):
            for y in range(newTam):
                if(j == 0 or j == height-1):
                    emptyImageInterpolation[i_run+x,j_run+y] = imgReal1[i,j]
                else:
                    value = (imgReal1[i,j].astype(np.intc) + imgReal1[i,j].astype(np.intc))/2
                    emptyImageInterpolation[i_run+x,j_run+y] = np.uint8(value)
        j_run += newTam
    j_run = 0
    i_run += newTam
cv2.imshow("Resultado Interpolacion",emptyImageInterpolation)

filename = 'ResultadoInterpolacion.jpg'
cv2.imwrite(filename, emptyImageInterpolation)

cv2.waitKey(0)
cv2.destroyAllWindows()