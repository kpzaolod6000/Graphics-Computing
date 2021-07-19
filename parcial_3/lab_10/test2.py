import cv2
# read an image
img = cv2.imread('rem.jpg', 1)
img = cv2.resize(img,(600,600))

# split the colour image and merge back
B, G, R = cv2.split(img)
img_BGR = cv2.merge((B,G,R))
img_RGB = cv2.merge((R,G,B))
img_BRG = cv2.merge((B,R,G))
img_GRB = cv2.merge((G,R,B))
print(B)
print(G)
print(R)

# display the merged images
cv2.imshow('Image in BGR', img_BGR)
cv2.imshow('Image in RGB', img_RGB)
cv2.imshow('Image in BRG', img_BRG)
cv2.imshow('Image in GRB', img_GRB)

cv2.waitKey(0)
cv2.destroyAllWindows() 
