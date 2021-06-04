import cv2
import numpy

# create your own gradient image
bphoto=numpy.empty(shape=(680,1277,3))
i=0
b=0
g=0
r=255
for g in range(256):
    bphoto[:,i]=[b,g,r]
    i=i+1
for r in range(1,256):
    r=255-r
    bphoto[:,i]=[b,g,r]
    i=i+1
for b in range(1,256):
    bphoto[:,i]=[b,g,r]
    i=i+1
for g in range(1,256):
    g=255-g
    bphoto[:,i]=[b,g,r]
    i=i+1
for r in range(1,256):
    bphoto[:,i]=[b,g,r]
    i=i+1
for b in range(1,256):
    b=255-b
    bphoto[:,i]=[b,g,r]


cv2.imwrite('bphoto.jpg',bphoto)
bphoto=cv2.imread('bphoto.jpg')

cv2.imshow('hi', bphoto)
cv2.waitKey()
cv2.destroyAllWindows()