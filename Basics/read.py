#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
# img = cv.imread('..Resources/Photos/cat_large.jpg')

cv.imshow('Cats', img)

# # Reading Videos
# 0 index for webcam or any other primary camera
# capture = cv.VideoCapture(0)
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    # break out of loop if d is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# wait for a specific delay for a key to be pressed. 
cv.waitKey(0) 
