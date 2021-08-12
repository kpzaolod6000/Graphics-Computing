import numpy as np
import cv2
 
cap = cv2.VideoCapture(0)
 
if False == cap.isOpened():
	# Pase la URL de la transmisión de video directamente a la función abierta de VideoCapture
    cap.open('http://192.168.0.108:8080/video')
 
while(True):
	 # Leer cuadro por cuadro
    ret, frame = cap.read()
    if Flase == ret:
       break
	 # Conversión directa a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
	
cap.release()
