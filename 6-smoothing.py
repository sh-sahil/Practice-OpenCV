import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur',gauss)

# Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median',median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 30, 20)
cv.imshow('Bileteral', bilateral)

cv.waitKey(0)