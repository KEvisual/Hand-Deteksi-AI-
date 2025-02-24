from hand_deteksi import HandDeteksi
import cv2

hand_deteksi = HandDeteksi(min_deteksi_confidence=0.5, min_tracking_confidence=0.5)

webcam = cv2.VideoCapture()
webcam.open(0, cv2.CAP_DSHOW)

while True:
    status , frame = webcam.read()
    frame = cv2.flip(frame,1)
    handLandMarks = hand_deteksi.findHandLandMarks(image=frame, draw=True)
    
    cv2.imshow("Rolzzz AI",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
webcam.release()