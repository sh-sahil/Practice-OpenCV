import cv2 as cv

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)

def changeRes(frame, scale = 0.2):
    '''Applicable on Images,Videos, and Live Videos'''
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# def reduceRes(width, height):
#     '''Only applicable on live Video'''
#     capture.set(3, width)
#     capture.set(4, height)


# resized_image = changeRes(frame =img)
# cv.imshow('Cat', resized_image)

# cv.waitKey(0)

#Reading the video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    resized_video = changeRes(500,500)
    # cv.imshow('Video',frame)
    cv.imshow('Video',resized_video)


    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()


