  
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../squareGris.jpg',0)
plt.hist(img.ravel(),256,[0,256]) 

plt.show()
#plt.savefig('hist.png')

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))

cv2.imshow('Equalized Image',res)
cv2.imwrite('Equalized Image.png',res)

plt.hist(res.ravel(),256,[0,256]) 

plt.show() 
#plt.savefig('equal-hist.png')


#OTRA FORMA
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# img = cv.imread('../squareGris.jpg',0)
# hist,bins = np.histogram(img.flatten(),256,[0,256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * float(hist.max()) / cdf.max()
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()