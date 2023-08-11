import cv2 as cv


# read image
img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)


# read video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()  # capture a video frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
