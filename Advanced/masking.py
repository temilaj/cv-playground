import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

# dimensions of the mask have to be the same size as the image
# blank = np.zeros((300,300), dtype='uint8')
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

# circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
# rectangular_mask = cv.rectangle(blank.copy(), (img.shape[1]//2 ,img.shape[0]//2),  (img.shape[1]//2 + 100,img.shape[0]//2 + 100), 255, -1)
circular_mask = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', circular_mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circular_mask,rectangle)
cv.imshow('Weird Shape', weird_shape)

# masked = cv.bitwise_and(img,img,mask=circular_mask)
masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)