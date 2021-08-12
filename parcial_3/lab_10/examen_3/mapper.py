import numpy as np

#Metodo para reordenar
def mapp(contours):
    contours = contours.reshape((4,2))

    Orderedcontours = np.zeros((4,2),dtype = np.float32)

    add = contours.sum(1) # suma los x + y 
    Orderedcontours[0] = contours[np.argmin(add)]
    Orderedcontours[3] = contours[np.argmax(add)]

    diff = np.diff(contours,axis = 1)# restar los x + y 
    Orderedcontours[1] = contours[np.argmin(diff)]
    Orderedcontours[2] = contours[np.argmax(diff)]

    return Orderedcontours
