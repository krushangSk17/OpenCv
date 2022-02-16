import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencvlogo.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#in GAUSSINAN ALWAYS TAKE POSITIVE AND ODD VALU OF K

blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#in this, TAKE POSITIVE AND ODD VALU OF size(k-kernal)
blur = cv2.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


blur = cv2.bilateralFilter(img,5,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('bilateral filter Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
