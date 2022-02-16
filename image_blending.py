import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('robo.jpg')
img2 = cv2.imread('open.jpg')
#IMAGE BLENDING

img3 = cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyWindow('img3')

#simple addition
img3 = 0.99*img2 + img1*0.01
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyWindow('img3')
