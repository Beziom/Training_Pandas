from tkinter import *

# Utworzenie okna głównego
root = Tk()
root.title("Leniwe przyciski")
root.geometry("200x85")

# Utworzenie w oknie ramkę do pomieszczenia obiektów
app = Frame(root) # ramka
app.grid() # umieszczenie

# Utworzenie w ramce przycisku
button1 = Button(app, text = "Nic nie robię!")
button1.grid()

#Utworzenie w ramce drugiego przycisku
button2 = Button(app) # Dodanie pustego przycisku
button2.grid()
button2.configure(text="Ja również!")

#Utworzenie trzeciego przycisku
button3 = Button(app)
button3.grid()
button3["text"] = "To samo mnie dotyczy"

root.mainloop()# Zamknięcie programu

