import numpy as np

def mapp(h):
    # print(h)
    h = h.reshape((4,2))
    # print(h)
    hnew = np.zeros((4,2),dtype = np.float32)
    # print(hnew)
    add = h.sum(1) # suma los x + y 
    # print(add)
    hnew[0] = h[np.argmin(add)]
    # print(np.argmin(add))
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h,axis = 1)
    # print(diff)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    # print(hnew)
    return hnew