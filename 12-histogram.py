import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# # histogram for gray scale
blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# circle = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
mask = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2), 200, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256], )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# Hostogram for the colored image

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask ,[256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
    
plt.show()

cv.waitKey(0)