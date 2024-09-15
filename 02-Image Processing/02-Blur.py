import cv2

img_path = "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg"
img = cv2.imread(img_path)


# Now we will blur the image
"""
To blur an image, we can use the cv2.GaussianBlur() function.
This function takes the following parameters:
1) the image you want to blur
2) the kernel size (a tuple of two integers), Which represents the width and height of the kernel
3) the standard deviation in the x-direction (if set to 0, the standard deviation will be calculated automatically)
"""
img = cv2.resize(img, (300, 300))
print(img.shape)
blur_img = cv2.GaussianBlur(img.copy(), (15, 15), 0)


cv2.imshow("original image", img)
cv2.imshow("blurred image", blur_img)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
