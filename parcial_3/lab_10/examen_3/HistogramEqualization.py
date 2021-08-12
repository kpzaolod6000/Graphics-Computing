import numpy as np

#HISTOGRAM EQUALIZATION
def getHistogramEqua(img,imageOut):
    histogramData = np.bincount(imageOut.flatten(),minlength=256)
    total_pixels = np.sum(histogramData)
    ##frecuencia
    Pn = histogramData/total_pixels
    #frecuencia acumulativa  
    Sn = np.cumsum(Pn)
    #floor
    Sn = np.floor(255*Sn).astype(np.uint8)
    # print(Sn)

    #matriz a lista
    img_list = list(img.flatten())
    #cambiando los colores con los valores ecualizados
    img_update = [Sn[i] for i in img_list]
    img_update = np.reshape(np.asarray(img_update),img.shape)
    return img_update