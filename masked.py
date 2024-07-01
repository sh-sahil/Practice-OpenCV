import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

cirlce = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(),(100,100), (400,400),255,-1)

wierd_image = cv.bitwise_and(cirlce, rectangle)
cv.imshow('wierd',wierd_image)


masked_image = cv.bitwise_and(img,img,mask = wierd_image)
cv.imshow('Masked Image', masked_image)

cv.waitKey(0)