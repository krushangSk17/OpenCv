import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('binary.png')
kernel  = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations=1)

cv2.imshow('original',img)
cv2.imshow('erosion',erosion)

dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('dilation',dilation)

#NOISE REMOVING METHOD

#opening method... first erosion adn after dilation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening',opening)


#closing method  first dilation and secon erosion
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing',closing)

#gradient method outline image
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('gradient',gradient)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat',blackhat)
cv2.imshow('tophat',tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)

# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)

# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
"""