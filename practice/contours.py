import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# Method 1 of finding contours
# 1. grayscale the image
# 2. blur the image, since we get too many contours if we use the original image
# 3. canny the image and get the edges
# 4. find the contours of the image of the cannied image

canny = cv.Canny(blur, 125, 175)

cv.imshow("Canny", canny)

contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')


# Method 2 of finding contours
# 1. grayscale the image
# 2. blur the image, since we get too many contours if we use the original image
# 3. binarize the image using the threshold function
# 4. find the contours of the image of the binarized image

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

cv.imshow("Thresh", thresh)

contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

# displaying the contours
# Creating a blank image to draw our contours on
blank = np.zeros(img.shape, dtype="uint8")
# drawing the contours
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)