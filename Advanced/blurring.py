#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
# computes pixel intensity of the middle pixel as the average
# of the surrounding pixel intensities
average = cv.blur(img, (3,3))
# average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
# similar to the avarage but in this case each surrounding pixel is given a particular weight
# the average of the products of those weights give you the value for the true center
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
# similar to average blur, but finds the median of the surrounding pixels instead of the average
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
# the most effective
# applies blurring but retails the edges in the image
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)