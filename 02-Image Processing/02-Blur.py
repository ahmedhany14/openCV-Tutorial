import cv2

img_path = "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg"
img = cv2.imread(img_path)

# to crop the image
"""
We will use the slicing method to crop the image.
This method takes the following parameters:
"""

crop_img = img[100:300, 100:300]

cv2.imshow("Cropped Image", crop_img)


if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
