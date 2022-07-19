#Przyciski utworzone za pomocą obiektów

from tkinter import *

class Application(Frame): # obiekty tpu Frame
    """Aplikacja oparta na GUI z trzema przyciskami"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utworzenie 3 przycisków które nic nie robią"""
        #Pierwszy przycisk
        self.button1 = Button(self,text = "Nic nie robię!")
        self.button1.grid()

        #Drugi przycisk
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text="Ja również!")

        #Trzeci przycisk
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "To samo mnie dotyczy"
#coś jeszcze
#część główna
root = Tk()
root.title("Leniwe przyciski 2.0")
root.geometry("210x85")
app = Application(root)
root.mainloop()