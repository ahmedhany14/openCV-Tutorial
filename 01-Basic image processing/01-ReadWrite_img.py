import cv2


# to read an image
"""
we use the cv2.imread() function to read an image.
this function takes the path of the image as an argument and returns the image in the form of a numpy array.
"""
img_path = "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg"
img = cv2.imread(img_path)

# 3D numpy array
print(img.shape)  # (height, width, channels)
print(img)  # the image in the form of a numpy array

# to display the image

"""
Use the cv2.imshow() function to display the image.
we need to pass the window name and the image as arguments to this function.
"""

cv2.imshow("image", img)

# to keep the window open until a key is pressed, if any number like 5000 is passed, the window will be closed after 5000 milliseconds,
# but if 0 is passed, the window will be closed when any key is pressed.
cv2.waitKey(1000)
cv2.destroyAllWindows()


# to write an image to a file

cv2.imwrite("new_img.jpg", img)
