# Fuctions that are used often in CV
import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('photo', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# blurring
blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny edges', canny)

# dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('dilated', dilated)

# erode the image
eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('eroded', eroded)

# resize the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# crop the image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)