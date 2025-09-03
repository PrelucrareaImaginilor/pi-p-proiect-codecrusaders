import cv2
from eye_tracking import EyeTracking

eyeTracking = EyeTracking()
webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    eyeTracking.refresh(frame)

    frame = eyeTracking.annotated_frame()
    cv2.imshow("Eye Tracking", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
