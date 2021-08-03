import cv2
cap = cv2.VideoCapture(0) #0 por defecto camera
cap.set(3,540)
cap.set(4,380)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break