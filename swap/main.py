# swapping images
# loading images
import cv2
goku=cv2.imread('goku.jpg')
amongus=cv2.imread('amongus.jpg')

#show goku
rgoku=cv2.rectangle(goku,(110,100),(380,400), (0,100,255), 3)
cv2.imshow('rgoku', rgoku)
cv2.waitKey()
cv2.destroyAllWindows()

#show amongus
ramongus=cv2.rectangle(amongus,(310,100),(580,400), (0,100,255), 3)
cv2.imshow('ramongus', ramongus)
cv2.waitKey()
cv2.destroyAllWindows()

#show cropped goku
cgoku=goku[100:400,110:380]
cv2.imwrite('cgoku.jpg',cgoku)
cv2.imshow('cgoku', cgoku)
cv2.waitKey()
cv2.destroyAllWindows()

#show cropped amongus
camongus=amongus[100:400,310:580]
cv2.imwrite('camongus.jpg',camongus)
cv2.imshow('camongus', camongus)
cv2.waitKey()
cv2.destroyAllWindows()

samongus=amongus
cv2.imshow('samongus', samongus)
cv2.waitKey()
cv2.destroyAllWindows()

#show swapped amongus
samongus[100:400,310:580]=cgoku
cv2.imshow('swamongus', samongus)
cv2.waitKey()
cv2.destroyAllWindows()

#show swapped amongus
samongus[100:400,310:580]=cgoku
cv2.imshow('swamongus', samongus)
cv2.waitKey()
cv2.destroyAllWindows()

sgoku=goku
cv2.imshow('sgoku', sgoku)
cv2.waitKey()
cv2.destroyAllWindows()

#show swapped goku
camongus=cv2.imread('camongus.jpg')
sgoku[100:400,110:380]=camongus
cv2.imwrite('sgoku.jpg',sgoku)
sgoku=cv2.imread('sgoku.jpg')
cv2.imshow('srgoku', sgoku)
cv2.waitKey()
cv2.destroyAllWindows()
