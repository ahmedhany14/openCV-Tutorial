import numpy as np
import cv2

# Corner detection
"""
The corner detection algorithm is used to detect the corners in an image. It is used in various applications like image stitching, object tracking, and 3D reconstruction.
this algorithm works with grayscale images

So at the first step, we need to convert the image to a grayscale image using the cv2.cvtColor() function.
This function takes the following parameters:
1) the image you want to convert
2) the color space you want to convert to (BG2GRAY)

Then we need to detect the corners in the image using the cv2.goodFeaturesToTrack() function.
This function takes the following parameters:
1) the grayscale image you want to detect the corners in
2) the maximum number of corners you want to detect
3) the quality level of the corners ([0: 1])
4) the minimum distance between the corners

This function returns a 2D array of the corners in the image.
"""

path = "/home/hany_jr/Ai/openCV-Tutorial/00-images/chessboard.png"

# load the image
image = cv2.imread(path)

image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# convert the image to grayscale
gray_img = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)

# detect the corners in the image

corners = cv2.goodFeaturesToTrack(gray_img.copy(), 100, 0.01, 10)


# Draw the corners on the image with circles
print(corners)
new_img = image.copy()
for corner in corners:

    x, y = int(corner[0][0]), int(corner[0][1])

    new_img = cv2.circle(new_img, (x, y), 5, (0, 255, 0), -1)

# Draw a line between all the corners

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = (int(corners[i][0][0]), int(corners[i][0][1]))
        corner2 = (int(corners[j][0][0]), int(corners[j][0][1]))
        # create a random color
        color = tuple(np.random.random(size=3) * 256)
        new_img = cv2.line(new_img, corner1, corner2, color, 1)

cv2.imshow("Corners", new_img)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
