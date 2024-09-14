import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # resize the frame
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Convert the image to HSV
    """
    HSV stands for Hue, Saturation, and Value. It is a color space that is used to separate the color information from the intensity information.
    to convert an image to the HSV color space, we need to use the cv2.cvtColor() function. It takes the following parameters:
    1) the image you want to convert
    2) the color space you want to convert to
    """

    # Convert the image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # we need to only detect the blue color in the image
    """
    1) we need to define the range of colors that we want to detect.
    2) we need to create a mask that will only show the blue color in the image, in the mask, the blue color will be white and the rest of the colors will be black.
    3) we need to apply the mask to the image to show only the blue color.
    """
    # define the range of blue color in HSV
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # create a mask that will only show the blue color in the image
    """
    To create a mask that will only show the blue color in the image, we need to use the cv2.inRange() function. It takes the following parameters:
    1) the image you want to create the mask for
    2) the lower range of the color you want to detect
    3) the upper range of the color you want to detect
    """
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    blue_img = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("HSV", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("Blue", blue_img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
