import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
def nothing(x):
    pass

#create trackbar
cv2.createTrackbar('H_l','image',0,179,nothing)
cv2.createTrackbar('S_l','image',0,255,nothing)
cv2.createTrackbar('V_l','image',0,255,nothing)

cv2.createTrackbar('H_h','image',0,179,nothing)
cv2.createTrackbar('S_h','image',0,255,nothing)
cv2.createTrackbar('V_h','image',0,255,nothing)

while(1):

    #take each frame
    _,frame = cap.read()
    frame = cv2.flip(frame,1)
    #convert bgr to hsv
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h_l = cv2.getTrackbarPos('H_l','image')
    s_l = cv2.getTrackbarPos('S_l', 'image')
    v_l = cv2.getTrackbarPos('V_l', 'image')
    h_h = cv2.getTrackbarPos('H_h', 'image')
    s_h = cv2.getTrackbarPos('S_h', 'image')
    v_h = cv2.getTrackbarPos('V_h', 'image')

    # define range of blue color in HSV
    lower_blue = np.array([h_l,s_l, v_l])
    upper_blue = np.array([h_h,s_h, v_h])
    #M_IMP IN BRACKET THAT IS HSV VALUE

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()