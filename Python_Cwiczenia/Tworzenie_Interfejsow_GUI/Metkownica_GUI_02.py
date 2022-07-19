from tkinter import *

#Utworzenie okna głównego
root = Tk()

#modyfikacja okna
root.title("Metkownica") # Tytuł głównego okna
root.geometry("450x200") # Wymiary

app = Frame(root) # utworzenie w oknie ramki jako pojemnik na widżety

app.grid() # posiadaja wszystkie widżety umożliwia rozplanowanie położenia

#utworzenie w ramce etykiety
etykieta = Label(app, text="Jestem erykietą!") #dzięki przekazaniu obietku app do konstruktora obiektu klasy Label ramka app staje się obiektem nadrzędnym
etykieta.grid() #zapewnienie widoczności etykiety

root.mainloop()