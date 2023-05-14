import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

from Herni_kamen import Herni_kamen

class Pozice(tk.Frame):
    def __init__(self, platno, hidden : bool, souradnice: tuple) -> None: # souradnice - [x, y]
        super().__init__(platno)
        self._platno = platno
        self._hidden = hidden
        self._aktualni_kamen = None
        self._souradnice = souradnice

        if(hidden == True):
            pass
        else:
            self.pozice_bg = Image.open("hint_piece.png") 
            #self.pozice_bg = self.pozice_bg.convert("RGBA")
            #background = Image.new("RGBA", self.pozice_bg.size, (255, 255, 255, 255))
            #composite = Image.alpha_composite(background, self.pozice_bg)
            self.pozice_bg_tk = ImageTk.PhotoImage(self.pozice_bg)
            self.kamen_button= Button(platno, image=self.pozice_bg_tk, command=lambda : Pozice.hint_clicked(self), bd=0, highlightthickness=0)
            self.kamen_button.config(width=self.pozice_bg_tk.width(), height=self.pozice_bg_tk.height())
            platno.create_window(souradnice[0], souradnice[1], window=self.kamen_button)


    @property
    def hidden(self) -> bool:
        return self._hidden

    @hidden.setter
    def hidden(self, value : bool):
        self._hidden = value
        
    @property
    def aktualni_kamen(self) -> Herni_kamen:
        return self._aktualni_kamen

    @aktualni_kamen.setter
    def aktualni_kamen(self, kamen : Herni_kamen):
        self._aktualni_kamen = kamen

    @property
    def get_souradnice(self) -> tuple:
        return self._souradnice

    def hint_clicked(self):
        print("HINT:")
        print(self._souradnice)

    def hidden_clicked(self):
        print("HIDDEN:")
        print(self._souradnice)