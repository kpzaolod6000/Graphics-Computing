import cv2

img = cv2.imread('rem.jpg', 1)
img = cv2.resize(img,(600,600))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,200,200)


if cv2.waitKey(1):
    cv2.destroyAllWindows()
cv2.imshow("imagen original",img)
cv2.imshow("imagen gray",imgGray)
cv2.imshow("imagencanny",imgCanny)

cv2.waitKey(0)#si se proporciona 0 como argumento, el usuario debe cerrar la ventana manualmente.
cv2.destroyAllWindows()