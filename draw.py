import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint a portion of the image
# blank[100:400, 100:400] = 0,255,0
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(blank,(100,100),(400,400),(0,255,0),thickness=2)
# cv.rectangle(blank,(100,100),(400,400),(0,255,0),thickness=-1)
# cv.rectangle(blank,(0,0),(blank.shape[0] // 2,blank.shape[0] // 2),(0,255,0),thickness=-1)
# cv.imshow('Reactangle', blank)

# 3. Circle
# cv.circle(blank, (blank.shape[0] // 2,blank.shape[0] // 2), 100, (0,0,255), thickness=3)
# cv.imshow('Circle', blank)

# 3. Draw a line
# cv.line(blank, (100,100), (400,400), (0,0,255), thickness=3)
# cv.imshow('Line', blank)

# 4. Write a text
cv.putText(blank,'Sahil Sharma', (100,200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=1)
cv.imshow('Text', blank)

cv.waitKey(0)