import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

from Herni_kamen import Herni_kamen

class Pozice(tk.Frame):
    def __init__(self, platno, hidden : bool, aktualni_kamen : Herni_kamen, souradnice) -> None: # souradnice - [point, pozice na pointu]
        super().__init__(platno)
        self._platno = platno
        self._hidden = hidden
        self._aktualni_kamen = aktualni_kamen
        self._souradnice = souradnice

        kamen_bg = Image.open("hint_piece.png")
        kamen_bg_tk = ImageTk.PhotoImage(kamen_bg)
        
        kamen_button.config(width=kamen_bg_tk.width(), height=kamen_bg_tk.height())
        if(self.hidden == True):
            kamen_button= Button(platno, image=kamen_bg_tk, command=lambda : ..., bd=0, bg="transparent", highlightcolor="", highlightthickness=0) 
        else:
            kamen_button= Button(platno, image=kamen_bg_tk, command=lambda : ..., bd=0, highlightthickness=0)
        platno.create_window(480, 300, window=kamen_button)

    @property
    def hidden(self) -> Herni_kamen:
        return self.hidden

    @hidden.setter
    def hidden(self, value : bool):
        self.hidden = value
        
    @property
    def aktualni_kamen(self) -> Herni_kamen:
        return self.aktualni_kamen

    @aktualni_kamen.setter
    def aktualni_kamen(self, kamen : Herni_kamen):
        self.aktualni_kamen = kamen

    @property
    def souradnice(self) -> list:
        return self.souradnice

    @souradnice.setter
    def aktualni_kamen(self, nove_souradnice : list):
        self.souradnice = nove_souradnice