import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Group', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=1)

print(f'No. of faces found {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)

# on Video
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# haar_cascade = cv.CascadeClassifier('haar_face.xml')
# while True:
#     isTrue, frame = capture.read()
#     face_rect = haar_cascade.detectMultiScale(frame,scaleFactor=1.1, minNeighbors=1)

#     for (x,y,w,h) in face_rect:
#         cv.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 2)

#     cv.imshow('Video',frame)

#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break
# capture.release()
# capture.destroyAllWindows()