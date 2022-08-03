import cv2 as cv
import numpy as np

# array filled with zeros
# uint8 = image type
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow("Blank", blank)

# 1. paint the image a certain color
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250, 250), (0,255,0), thickness=2)
# cv.rectangle(blank, (0,0), (250, 250), (0,255,0), thickness=-1)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=2)
# cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
# cv.imshow('Line', blank)

# 5. Writing Text
cv.putText(blank, "Welcome Kyle", (100,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)