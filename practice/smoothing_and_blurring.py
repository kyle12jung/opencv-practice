import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow("Original", img)

# Averaging
# takes the window and applies the pixel intensity of the middle tile to the average of the surrounding tiles
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

# Gaussian Blur
# the middle tile is the average of the weights of the surrounding tiles
# less blurry, plus more natural
# sigmaX = s.t.d of the x direction (currently 0)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gauss', gauss)


# Median Blur
# meant to be used for smaller kernal sizes (preferrably under 3)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
# Better results
# Higher sigmaColor and sigmaSpace, similar to median blur
# takes into account the edges
bilateral = cv.bilateralFilter(img, 10, 25, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)