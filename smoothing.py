import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)

# Averaging blur
average = cv.blur(img, (5, 5))
cv.imshow('Average blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Gaussian blur', gauss)

# Median blur
median = cv.medianBlur(img, 5)
cv.imshow('Median blur', median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur', bilateral)

cv.waitKey(0)