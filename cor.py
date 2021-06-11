import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def draw_plan():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.hands
    hands = mpHand.Hands()
    mpDraw = mp.solutions.drawing_utils
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
    # print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handlms)
            cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()

draw_plan()