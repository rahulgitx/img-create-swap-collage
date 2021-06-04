import cv2 
import numpy

#shows image 1
naruto=cv2.imread('naruto.jpg')
cv2.imshow('naruto',naruto)
cv2.waitKey()
cv2.destroyAllWindows()

#shows image 2
opm=cv2.imread('opm.jpg')
cv2.imshow('opm',opm)
cv2.waitKey()
cv2.destroyAllWindows()

#shows image 3
tg=cv2.imread('tg.jpg')
cv2.imshow('tg',tg)
cv2.waitKey()
cv2.destroyAllWindows()

#shows image 4
dbz=cv2.imread('dbz.jpg')
cv2.imshow('dbz',dbz)
cv2.waitKey()
cv2.destroyAllWindows()


#shows the collage
photo=numpy.empty(shape=(780,1277,3))
photo[:,:]=[133,133,133]
opm=cv2.imread('opm.jpg')
photo[0:434,572:1277]=opm
photo[411:780,602:1277 ]=dbz
photo[0:779,0:623]=tg
photo[60:712,450:811]=naruto
cv2.imwrite('opmphoto.jpg',photo)
opmphoto=cv2.imread('opmphoto.jpg')
cv2.imshow('opmphoto',opmphoto)
cv2.waitKey()
cv2.destroyAllWindows()