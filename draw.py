import cv2 as cv
import numpy as np

# img = cv.imread('Photos/cats.jpg')
# cv.imshow('Cat', img)

# create blank image
#uint8 is the datatype of an images
# set to an array of height, width and the number of color channels
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# # 1. Paint the image a certain colour
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red square', blank)

# # 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,350), (0,255,0), thickness=2)
# cv.rectangle(blank, (0,0), (250,350), (0,255,0), thickness=cv.FILLED)
# cv.FILLED = -1
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# # 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 60, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# # 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# # 5. Write text
cv.putText(blank, 'Hello, from Temi!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)