import numpy as np
import cv2


# 1) Open the camera
"""
To capture a video, you need to create a VideoCapture object. Its argument can be either the device index or the name of a video file.
Device index is just the number to specify which camera. Normally one camera will be connected (as in my case). So I simply pass 0 (or -1).
You can select the second camera by passing 1 and so on. After that, you can capture frame-by-frame. But at the end, don’t forget to release the capture.
"""

cap = cv2.VideoCapture(0)

# 2) Capture the video frame by frame

while True:
    # get a frame

    # ret is a boolean variable that returns true if the frame is available. It reads the frames from the video file one by one.
    # frame is the actual image frame captured from the camera.
    ret, frame = cap.read()

    # get the height and width of the frame
    height, width = frame.shape[:2]

    resized_image = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    smaller_frame = np.zeros((height, width, 3), dtype=np.uint8)
    smaller_frame.fill(90)
    smaller_frame[height // 2 :, width // 2 :] = resized_image
    smaller_frame[: height // 2, : width // 2] = resized_image
    smaller_frame[height // 2 :, : width // 2] = resized_image
    smaller_frame[: height // 2, width // 2 :] = resized_image

    # 3) Display the resulting frame
    cv2.imshow("frame", smaller_frame)

    # here it will wait for 1ms and then it will capture the next frame, if you press 'q' it will break the loop and close the camera
    if cv2.waitKey(1) == ord("q"):
        break


# 4) Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
