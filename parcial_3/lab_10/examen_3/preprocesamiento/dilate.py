import cv2
import numpy as np
from matplotlib import pyplot as plt

imgReal1 = cv2.imread("imgGC.jpg") #8 bit por escala de grises
img1 = imgReal1.copy()

imgReal2 = cv2.imread("Propio_imgGC.jpg") #8 bit por escala de grises
img2 = imgReal2.copy()
height,width, channels=img2.shape

cv2.imshow("Image Original 1", img1)
cv2.imshow("Image Original 2", img2)

#DILATE PROPIO
# tranformnd a bin
imgBin = img2 * (1/255)
imgBin = np.uint8(imgBin)
print(imgBin)

MyimgDilate = img2.copy()
kernel = np.uint8(np.ones((5,5)))
print(kernel)
center = len(kernel)//2
for i in range(center,len(imgBin)-center):
    for j in range(center,len(imgBin[i])-center):
        # print(imgBin[i,j])
        for x in range(len(kernel)):
            for y in range(len(kernel[x])):
                k = i - center + x
                l = j - center + y
                #OR OPERATOR
                # if (img2[k,l] == 0 and kernel[x,y] == 0):
                #     result = np.uint8(255) # 0
                # else:
                #     result = np.uint8(0)# 1

                result = imgBin[k,l] | kernel[x,y] 
                print(result)
                result = result*255
                MyimgDilate[k,l] = result

            
cv2.imshow("Image Propio Dilate", MyimgDilate)





#DILATE USANDO LIBRERIA

imgDial = cv2.dilate(img1 ,kernel,iterations = 2)
cv2.imshow("Image Dilate", imgDial)
    

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()