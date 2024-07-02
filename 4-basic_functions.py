import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur an image
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=1)
# cv.imshow('Dilated Image', dilated)

# Eroding 
# eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resize the image
# resize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resize', resize)

# Cropping the images
cropped = img[100:300, 100:300]
cv.imshow('Cropped', cropped)
cv.waitKey(0)