import cv2


# url = "http://admin:admin@192.168.3.11:8081"
# El programa se está ejecutando, pero la cámara no está encendida
# url = "http://admin:123456@192.168.3.16:8081"
# Enciende la cámara correctamente

url = "rtsp://admin:admin@192.168.1.8:8554/live"
# Devolver el error directamente: [rtsp @ 000001ee2b0824c0] falló el método DESCRIBE: 401 no autorizado

# url = "rtsp://admin:123456@192.168.3.16:8554/live"
# [rtsp @ 0000019250a424c0] el método DESCRIBE falló: 404 Stream Not Found La cámara del teléfono se encenderá y el programa informará un error

print('start')
cap = cv2.VideoCapture(url)#Read video stream
while(cap.isOpened()):
    ret, frame = cap.read()
    print('success')
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()