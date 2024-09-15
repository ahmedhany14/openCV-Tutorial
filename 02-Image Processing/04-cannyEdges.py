import cv2

img_path = "/home/hany_jr/Ai/openCV-Tutorial/00-images/img1.jpeg"
img = cv2.imread(img_path)


"""
The canny function is different from the corner detection algorithm.
The corner detection algorithm is used to detect the corners in an image, while the canny function is used to detect the edges in an image.
"""

# To find the edges in an image, we can use the cv2.Canny() function.
"""
This function takes the following parameters:
1) the image you want to find the edges in
2) the lower threshold
3) the upper threshold
"""

lowers = 100
uppers = 200

edges = cv2.Canny(img.copy(), lowers, uppers)
cv2.imshow("edges", edges)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
