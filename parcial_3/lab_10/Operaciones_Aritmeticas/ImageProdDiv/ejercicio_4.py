import cv2
import numpy as np

imgReal1 = cv2.imread("pug.jpg",1) #8 bit por escala de grises
imgReal1 = cv2.resize(imgReal1,(400,400))
img1 = imgReal1

imgReal2 = cv2.imread("magico.jpg",1) #8 bit por escala de grises
imgReal2 = cv2.resize(imgReal2,(400,400))
img2 = imgReal2

cv2.imshow("Image Original 1", imgReal1)
cv2.imshow("Image Original 2", imgReal2)

B1, G1, R1 = cv2.split(img1)
B2, G2, R2 = cv2.split(img2)
B1, G1, R1 = B1.astype(int), G1.astype(int), R1.astype(int)
B2, G2, R2 = B2.astype(int), G2.astype(int), R2.astype(int)
Bresult,Gresult,Rresult = B1.copy(), G1.copy(), R1.copy()

X = [0.25,0.5,0.75]
for x in X:
    for i in range(len(B1)):
        for j in range(len(B1[0])):
           
            Bresult[i,j] =  x*B1[i, j] + (1-x)*B2[i, j]
            Gresult[i,j] =  x*G1[i, j] + (1-x)*G2[i, j]    
            Rresult[i,j] =  x*R1[i, j] + (1-x)*R2[i, j]

    img_result = cv2.merge((Bresult,Gresult,Rresult))
    img_result = np.array(img_result, dtype=np.uint8)
    title_ = "Resultado_con_constante_C_=_"+str(x)
    cv2.imshow(title_, img_result)

    # filename = "Resultado_con_constante_C_=_"+str(x)+".jpg"
    # cv2.imwrite(filename, img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()