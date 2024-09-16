import numpy as pd
import cv2


# thresholding

"""
To apply thresholding, we use the cv2.threshold() function.
It takes the following arguments:
    - src: The source image.
    - thresh: The threshold value.
    - maxval: The maximum value that can be assigned to the pixels.
    - type: The type of thresholding to be applied. (like cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV)
"""


img = cv2.imread("/home/hany_jr/Ai/openCV-Tutorial/00-images/soccer_practice.jpg")

img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

cv2.imshow("Original", img)


# 1) Simple Thresholding
threshold, thresh = cv2.threshold(img.copy(), 225, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", thresh)

threshold_inv, thresh_inv = cv2.threshold(img.copy(), 225, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Inverse", thresh_inv)



if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
