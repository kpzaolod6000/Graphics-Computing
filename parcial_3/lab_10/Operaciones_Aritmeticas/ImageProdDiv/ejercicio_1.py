import cv2
import numpy as np

imgReal1 = cv2.imread("tigre.jpg", 1) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1

cv2.imshow("Image Original 1", imgReal1)

img1 = img1.astype(int)
constantes = [2,5,7]

B, G, R = cv2.split(img1)
Bresult,Gresult,Rresult = B.copy(), G.copy(), R.copy()
for c in constantes:
    for i in range(len(img1)):
        for j in range(len(img1[0])):

            sum_B = B[i,j]*c
            if sum_B > 255 :
                Bresult[i,j] = 255
            else:
                Bresult[i,j] = sum_B
            
            sum_G = G[i,j]*c
            if sum_G > 255 :
                Gresult[i,j] = 255
            else:
                Gresult[i,j] = sum_G

            sum_R = R[i,j]*c
            if sum_R > 255 :
                Rresult[i,j] = 255
            else:
                Rresult[i,j] = sum_R
                
    img_result = cv2.merge((Bresult,Gresult,Rresult))
    img_result = np.array(img_result, dtype=np.uint8)
    title_ = "Resultado con constante c = "+ str(c)
    cv2.imshow(title_, img_result)
    # filename = "Resultado_C = "+str(c)+".jpg"
    # cv2.imwrite(filename, img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()