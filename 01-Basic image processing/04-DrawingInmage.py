import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # 1) to draw a line on the image, we need to use the cv2.line() function
    """
    It takes the following parameters:
    1) the image on which you want to draw the line
    2) the starting and ending point of the line (x, y)
    3) the color of the line (BGR)
    4) the thickness of the line or the width of the line
    """
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    height, width = frame.shape[:2]

    # draw a line from the top left corner to the bottom right corner
    line_img = cv2.line(frame.copy(), (0, 0), (width, height), (156, 123, 54), 20)
    # draw a line from the top right corner to the bottom left corner, to make a X shape
    line_img = cv2.line(line_img, (0, height), (width, 0), (56, -9, 15), 20)

    # 2) to draw a rectangle on the image, we need to use the cv2.rectangle() function
    """
    1) the image on which you want to draw the rectangle
    2) the top-left corner of the rectangle (x, y)
    3) the bottom-right corner of the rectangle (x, y)
    4) the color of the rectangle (BGR)
    5) the thickness of the rectangle or the width of the rectangle if -1 is passed, it will fill the rectangle with the color
    """

    rectangle_img = cv2.rectangle(
        frame.copy(), (100, 100), (200, 250), (0, 255, 0), 120
    )

    # 3) to draw a circle on the image, we need to use the cv2.circle() function
    """
    1) the image on which you want to draw the circle
    2) the center of the circle (x, y)
    3) the radius of the circle
    4) the color of the circle (BGR)
    5) the thickness of the circle or the width of the circle if -1 is passed, it will fill the circle with the color
    """

    circle_img = cv2.circle(
        frame.copy(), (width // 2, height // 2), 100, (255, 0, 0), 10
    )

    # 4) Add text to the image
    """
    To add text to the image, we need to use the cv2.putText() function. It takes the following parameters:
    1) the image on which you want to draw the text
    2) the text you want to write
    3) the position where you want to write the text (x, y)
    4) the font you want to use
    5) the font size, or boldness of the text
    6) the color of the text (BGR)
    7) the thickness of the text
    """

    text_img = cv2.putText( 
        frame.copy(),
        "Ahmed hany is here right now",
        (0, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (255, 255, 255),
        2,
    )

    cv2.imshow("frame", frame)
    cv2.imshow("line", line_img)
    cv2.imshow("rectangle", rectangle_img)
    cv2.imshow("circle", circle_img)
    cv2.imshow("text", text_img)
    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
