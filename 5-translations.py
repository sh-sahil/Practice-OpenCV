import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation
# def translate(img, x, y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)


# translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)


# Rotation
# def rotate(img, angle, rotPoint = None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)

#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.5)
#     dimensions = (width, height)

#     return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img , 45)
# cv.imshow('rotated', rotated)

# Resizing
# resize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resize', resize)

# Flipping the images
# flip = cv.flip(img, 1)
# cv.imshow('Vertical FLip', flip)
# flip = cv.flip(img, 0)
# cv.imshow('Horizontal FLip', flip)
# flip = cv.flip(img, -1)
# cv.imshow('Diagonal FLip', flip)

# Cropping
cropped = img[100:300, 100:300]
cv.imshow('Cropped', cropped)


cv.waitKey(0)