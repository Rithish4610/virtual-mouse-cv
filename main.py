import cv2
import mediapipe as mp
import pyautogui

# Screen size
screen_width, screen_height = pyautogui.size()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_img)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger = hand_landmarks.landmark[8]
            thumb = hand_landmarks.landmark[4]

            x = int(index_finger.x * w)
            y = int(index_finger.y * h)

            screen_x = int(index_finger.x * screen_width)
            screen_y = int(index_finger.y * screen_height)

            pyautogui.moveTo(screen_x, screen_y)

            distance = abs(index_finger.x - thumb.x)

            if distance < 0.02:
                pyautogui.click()

    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
