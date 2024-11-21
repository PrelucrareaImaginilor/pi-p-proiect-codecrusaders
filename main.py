from script import detect_eyes
import tkinter as tk
from tkinter import simpledialog

def main():
    root = tk.Tk()
    root.withdraw() # asteptam input-ul
    imaginea = tk.simpledialog.askstring("Input nume imagine", "Introdu numele imaginii si extensia ei: ")
    if imaginea:
        detect_eyes("Imagini/" + imaginea)
    else:
        print("Nu am primit nume de fisier.")

    root.destroy()


if __name__ == "__main__":
    main()
