import cv2

img_path = "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg"
img = cv2.imread(img_path)

cv2.imshow("original image", img)

# to resize the image
img = cv2.resize(img, (400, 400))  # resize the image to 200x200 pixels
cv2.imshow("resized image", img)


# rotate the image
"""
we can rotate an image using the cv2.rotate() function.
this function takes the image and the rotation flag as arguments.
the rotation flag can be one of the following:
cv2.ROTATE_90_CLOCKWISE: rotate the image 90 degrees clockwise
cv2.ROTATE_180: rotate the image 180 degrees
cv2.ROTATE_90_COUNTERCLOCKWISE: rotate the image 90 degrees counterclockwise

"""

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # rotate the image 90 degrees clockwise
cv2.imshow("rotated image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
