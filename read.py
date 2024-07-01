import cv2 as cv

#Reading images
# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)


#Reading the video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.release()
capture.destroyAllWindows()

