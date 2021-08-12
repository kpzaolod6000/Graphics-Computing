import cv2
import numpy as np
from matplotlib import pyplot as plt

imgReal1 = cv2.imread("hoja2.jpg", cv2.IMREAD_GRAYSCALE) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(300,300))
img1 = imgReal1.copy()

#Propio KERNEL GAUSSIAN BLUR
kernelGauss = np.array([[ 1, 4, 6, 4,1],
                        [ 4,16,24,16,4],
                        [16,24,36,24,6],
                        [ 4,16,24,16,4],
                        [ 1, 4, 6, 4,1]])
# print(kernelGauss)
kernelGauss = kernelGauss * (1/256)
# print(kernelGauss)
MyimgBlur = img1.copy()

center = len(kernelGauss)//2
# print(center)
for i in range(center,len(img1)-center):
    for j in range(center,len(img1[i])-center):
        sum_ = 0
        for x in range(len(kernelGauss)):
            for y in range(len(kernelGauss[x])):
                k = i - center + x
                l = j - center + y

                multiPixel = img1[k,l].astype(float) * kernelGauss[x,y]
                sum_ += multiPixel
        if sum_ > 255:
            MyimgBlur[i,j] = np.uint8(255)
        else:    
            MyimgBlur[i,j] = np.uint8(sum_)
        # print(img1[i,j])
cv2.imshow("Image Propia BlurGaussian", MyimgBlur)
MyimgCanny = cv2.Canny(MyimgBlur,200,200) #era 200
print(MyimgCanny.shape)
cv2.imshow("Image Canny", MyimgCanny)
# filename = 'Propio_imgGC.jpg'
# cv2.imwrite(filename, MyimgCanny)

#PROPIO DILATE
MyimgDilate = MyimgCanny.copy()
kernelDi = np.ones((5,5)) * 255
kernelDi = np.uint8(kernelDi)
print(kernelDi)

center = len(kernelDi)//2
for i in range(center,len(MyimgCanny)-center):
    for j in range(center,len(MyimgCanny[i])-center):
        # print(imgBin[i,j])
        isEqual = False
        for x in range(len(kernelDi)):
            for y in range(len(kernelDi[x])):
                k = i - center + x
                l = j - center + y
                if (MyimgCanny[k,l] == kernelDi[x,y]):
                    isEqual = True
        if isEqual:        
            MyimgDilate[i,j] = np.uint8(255)
        else:
            MyimgDilate[i,j] = np.uint8(0)
cv2.imshow("Image Propia Dilate", MyimgDilate)

#PROPIO EROTION
MyimgErode = MyimgDilate.copy()

for i in range(center,len(MyimgDilate)-center):
    for j in range(center,len(MyimgDilate[i])-center):
        # print(imgBin[i,j])
        isEqual = False
        for x in range(len(kernelDi)):
            for y in range(len(kernelDi[x])):
                k = i - center + x
                l = j - center + y
                if (MyimgDilate[k,l] != kernelDi[x,y]):
                    isEqual = True
        if isEqual:        
            MyimgErode[i,j] = np.uint8(0)
        else:
            MyimgErode[i,j] = np.uint8(255)
cv2.imshow("Image Propia Erode", MyimgErode)


#Usando librerias
imgBlur = cv2.GaussianBlur(img1,(5,5),1)# para reducir el ruido
imgCanny = cv2.Canny(imgBlur,200,200) #era 200
imgDial = cv2.dilate(imgCanny ,kernelDi,iterations = 1) # 2 ITERACIONES y en mi caso es una iteracion
imgErode = cv2.erode(imgDial,kernelDi,iterations = 1)

cv2.imshow("Image Original 1", img1)
cv2.imshow("Image Original BlurGaussian", imgBlur)
cv2.imshow("Image Original Canny", imgCanny)
cv2.imshow("Image Original Dilate", imgDial)
cv2.imshow("Image Original Erodee", imgErode)
# filename = 'imgGC.jpg'
# cv2.imwrite(filename, imgCanny)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()