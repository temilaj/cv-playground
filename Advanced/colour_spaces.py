#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# # BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# # BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)
# plt.imshow(rgb)
# plt.show()


# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV => BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow('LAB --> BGR', lab_bgr)

# You can't convert gray scale images to HSV directly. If you want to do that You first go Grayscale -> BGR -> HSV
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('Gray => BGR', hsv_bgr)
bgr_hsv = cv.cvtColor(gray_bgr, cv.COLOR_BGR2HSV)
cv.imshow('BGR => HSV', bgr_hsv)

cv.waitKey(0)