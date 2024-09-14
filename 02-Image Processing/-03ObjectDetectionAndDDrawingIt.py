import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8l")

names = {
    0: "person",
    32: "sports ball",
}


def load_image(image_path):
    image = cv2.imread(image_path)
    return image


def predict(image):
    predictions = model(image, save=False)
    return predictions


def extract_results(outputs):
    objects = []
    for result in outputs:
        boxes = result.boxes.cpu().numpy()  # Boxes object for bounding box outputs
        for i in range(len(boxes)):
            # Extract the class ids
            class_id = int(boxes.cls[i])
            if class_id not in names:
                continue
            # Extract the coordinates of the bounding box
            x1, y1, x2, y2 = boxes.xyxy[i]

            # Create a dictionary containing the class id, name, and coordinates
            properties = {
                "id": class_id,
                "name": names[class_id],
                "corner1": (int(x1), int(y1)),
                "corner2": (int(x2), int(y2)),
            }

            # Append the dictionary to the objects list
            objects.append(properties)

    # Return the list of objects
    return objects


def draw_boxes(boxes, image):
    new_image = image.copy()

    for box in boxes:
        print(box)
        x1, y1 = box["corner1"]
        x2, y2 = box["corner2"]
        if box["name"] == "person":
            cv2.rectangle(new_image, (x1, y1), (x2, y2), (0, 255, 0), 4)
        else:
            cv2.rectangle(new_image, (x1, y1), (x2, y2), (255, 0, 0), 4)
        cv2.putText(
            new_image,
            box["name"],
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (56, 16, 87),
            2,
        )
    cv2.imshow("Image", new_image)
    return


def photo_drawing():
    """
    Here i will put the path of the image and call the functions
    1. Load the image
    2. Predict the image
    3. Extract the boxes
    4. Draw the boxes
    """
    path = "/home/hany_jr/Ai/openCV-Tutorial/00-images/soccer_practice.jpg"
    image = load_image(path)

    # cv2.imshow("Image", image)
    resultOfModel = predict(image.copy())

    boxes = extract_results(resultOfModel)

    draw_boxes(boxes, image)


def capture_drawing():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resultOfModel = predict(frame.copy())
        boxes = extract_results(resultOfModel)
        draw_boxes(boxes, frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


# photo_drawing()
capture_drawing()


if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
