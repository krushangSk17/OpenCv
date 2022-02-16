import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass

img = cv2.imread('kohli.jfif',0)
cv2.namedWindow('image')


#create trackbar
cv2.createTrackbar('n','image',0,1000,nothing)
cv2.createTrackbar('m','image',0,1000,nothing)

while(1):
    min = cv2.getTrackbarPos('n','image')
    max = cv2.getTrackbarPos('m', 'image')

    edges = cv2.Canny(img,min,max)

    cv2.imshow('original',img)
    cv2.imshow('edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()