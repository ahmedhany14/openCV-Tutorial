import cv2


# to change the color of the image
"""
There are many ways to change the color of an image.
cv2.IMREAD_COLOR: It is the default flag. It specifies to load a color image. or -1
cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. or 0
cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. or 1
"""

img = cv2.imread(
    "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg", -1
)  # original image
cv2.imshow("original image", img)

cv2.waitKey(2000)

img = cv2.imread(
    "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg", 0
)  # grayscale image
cv2.imshow("grayscale image", img)

cv2.waitKey(2000)

img = cv2.imread(
    "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg", 1
)  # color image
cv2.imshow("color image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
