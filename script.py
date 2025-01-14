import cv2 as cv

def detect_and_track_eyes():
    # Incarc clasificatorul Haar pentru ochi și fata
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if eye_cascade.empty() or face_cascade.empty():
        print('Eroare: clasificatorul în cascada nu a fost încarcat.')
        return

    # Deschide camera
    cap = cv.VideoCapture(0)  # Schimbă indexul dacă e necesar
    if not cap.isOpened():
        print("Eroare: Camera nu a putut fi deschisă.")
        return

    # Inițializare trackeri pentru fiecare ochi
    tracker_left = cv.TrackerCSRT_create()
    tracker_right = cv.TrackerCSRT_create()
    tracking_active = False

    def is_eye_region(bbox, face_bbox):
        # Verific regiunea
        x, y, w, h = bbox
        face_x, face_y, face_w, face_h = face_bbox
        # Dimensiunea minimă și maxima rezonabilă pentru un ochi
        min_size, max_size = (15, 15), (60, 60)
        if w < min_size[0] or h < min_size[1] or w > max_size[0] or h > max_size[1]:
            return False
        # Verificam pozitia în raport cu fata
        if not (face_x < x < face_x + face_w and face_y < y < face_y + face_h // 2):
            return False
        return True

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Eroare: Nu am putut citi frame-ul de la camera.")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if not tracking_active:
            # Detectam fața pentru a avea un context
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            if len(faces) > 0:
                face = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)[0]  # Cea mai apropiata fata de camera
                x, y, w, h = face
                cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Detectare ochi in interiorul fetei
                roi_gray = gray[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5)

                valid_eyes = [eye for eye in eyes if is_eye_region((eye[0] + x, eye[1] + y, eye[2], eye[3]), face)]
                if len(valid_eyes) >= 2:
                    # Sortam ochii dupa coordonata x
                    valid_eyes = sorted(valid_eyes, key=lambda e: e[0])

                    # Initializare tracker
                    tracker_left.init(frame, tuple((valid_eyes[0][0] + x, valid_eyes[0][1] + y, valid_eyes[0][2], valid_eyes[0][3])))
                    tracker_right.init(frame, tuple((valid_eyes[1][0] + x, valid_eyes[1][1] + y, valid_eyes[1][2], valid_eyes[1][3])))
                    tracking_active = True
        else:
            # Actualizez pozitiile ochilor
            success_left, bbox_left = tracker_left.update(frame)
            success_right, bbox_right = tracker_right.update(frame)

            if success_left:
                x, y, w, h = map(int, bbox_left)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if success_right:
                x, y, w, h = map(int, bbox_right)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # daca se pierde detectia unui ochi, se va relua din nou procesu de detectare
            if not success_left or not success_right:
                tracking_active = False

        # Afisam frame-ul
        cv.imshow('Tracking ochi individual', frame)


        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
