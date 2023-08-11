import cv2 as cv


def change_resolution(width, height):
    # Live Video
    capture.set(3, width)
    height.set(4, height)


def rescale_frame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# read image
img = cv.imread('Resources/Photos/cat.jpg')

resized_image = rescale_frame(img)
cv.imshow('Cat', resized_image)

cv.waitKey(0)


# read video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()