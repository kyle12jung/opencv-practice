import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# SIMPLE THRESHOLDING

# binarizing image
# threshold = the threshold value passed in (150)
# 150 above gets converted into 255, below to 0
# thresh is the binarized image
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded", thresh)
# inverse binarizing
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded INV", thresh_inv)

# Adaptive Thresholding
# C = the value to be subtracted from the mean
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)