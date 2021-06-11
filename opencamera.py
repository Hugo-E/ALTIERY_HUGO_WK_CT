import cv2

#Open camera
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    #Check error
    if not ret:
        print("Unable to open camera\n")
        break
    #Show camera
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Name", frame)
    #Close the window
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()