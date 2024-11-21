import cv2 as cv
import time

def detect_eyes(image_path):
    #Dam start la cronometru:
    start_cronometru = time.perf_counter()
    # Incarc clasificatorul in cascada Haar pentru detectia ochilor
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    if eye_cascade.empty():
        print('Eroare: clasificator în cascadă pentru ochi nu a fost incarcat.')
        return

    # citesc imaginea si verific daca a fost incarcata cu succes
    img = cv.imread(image_path)
    if img is None:
        print("Eroare. Nu am putut incarca imaginea")
        return

    # Convertim imaginea la alb-negru
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # aplicam metoda detectMultiScale pentru a detecta ochii
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # for-ul urmator are ca scop crearea unui chenar in care sunt incadrati ochii gasiti de algoritm
    for (x, y, w, h) in eyes:
        # Reducem dimensiunea acestui chenar
        shrink_factor = 0.25
        shrink_w = int(w * shrink_factor)
        shrink_h = int(h * shrink_factor)
        smaller_x = x + shrink_w
        smaller_y = y + shrink_h
        smaller_w = w - 2 * shrink_w
        smaller_h = h - 2 * shrink_h

        # desenam chenarul folosind metoda rectangle din openCV
        cv.rectangle(img, (smaller_x, smaller_y), (smaller_x + smaller_w, smaller_y + smaller_h), (0, 255, 0), 2)

    timp = (time.perf_counter() - start_cronometru)*1000
    print(f"Timpul de executie al algoritmului este de {timp:.2f} milisecunde.")
    cv.imshow('Detectarea ochilor', img) # Afisam imaginea
    #cv.imshow("Grayscale", gray)
    cv.waitKey(0) # La apasarea unei taste, programul se va opri si ferestrele vor fi inchise
    cv.destroyAllWindows()