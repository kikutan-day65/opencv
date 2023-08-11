import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Original', img)

# Translation
def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, trans_mat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, -100) 
cv.imshow('Translated', translated)

# Rotate
def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width // 2, height // 2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rot_mat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flipped = cv.flip(img, 0)
cv.imshow('Flipped', flipped)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)