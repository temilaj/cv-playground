#pylint:disable=no-member

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# wait for a specific delay for a key to be pressed. 
cv.waitKey(0) 
