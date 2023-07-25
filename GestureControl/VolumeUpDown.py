import cv2
import mediapipe as mp
import pyautogui
import math

x1 = y1 = x2 = y2 = 0
# This particular code will capture Webcam's image
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, image = webcam.read()
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # This part of code will convert image to RGB color gamete
    output = my_hands.process(rgb_image)  # This is for the processing part
    hands = output.multi_hand_landmarks
    key = cv2.waitKey(1) & 0xFF
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

        # Adjust the threshold value based on your hand gestures and camera resolution
        threshold = 50
        if dist > threshold:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    cv2.imshow("Hand Volume control using Python!!", image)
    cv2.waitKey(10)  # This function will keep a delay of 10 milliseconds
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
