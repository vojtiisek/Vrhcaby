import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

import SoundManager
from Herni_kamen import Herni_kamen
from Mapa_kamenu import Mapa_kamenu
from Mapa_pozic import Mapa_pozic

class Pozice(tk.Frame):
    def __init__(self, platno, hidden : bool, souradnice: list) -> None: # souradnice - [x, y]
        super().__init__(platno)
        self._platno = platno
        self._hidden = hidden
        self._souradnice = souradnice

        if(hidden == True):
            pass
        else:
            self.pozice_bg = Image.open("hint_piece.png") 
            self.pozice_bg_tk = ImageTk.PhotoImage(self.pozice_bg)
            self.kamen_button= Button(platno, image=self.pozice_bg_tk, command=lambda : Pozice.hint_clicked(self), bd=0, highlightthickness=0)
            self.kamen_button.config(width=self.pozice_bg_tk.width(), height=self.pozice_bg_tk.height())
            platno.create_window(souradnice[0], souradnice[1], window=self.kamen_button)


    @property
    def hidden(self) -> bool:
        return self._hidden

    def set_hidden(self, value : bool):
        if(value):
            ...
        else:
            self.pozice_bg = Image.open("hint_piece.png") 
            self.pozice_bg_tk = ImageTk.PhotoImage(self.pozice_bg)
            self.kamen_button= Button(self._platno, image=self.pozice_bg_tk, command=lambda : Pozice.hint_clicked(self), bd=0, highlightthickness=0)
            self.kamen_button.config(width=self.pozice_bg_tk.width(), height=self.pozice_bg_tk.height())
            self._platno.create_window(self._souradnice[0], self._souradnice[1], window=self.kamen_button, tags="mozny_tah")

    @property
    def get_souradnice(self) -> tuple:
        return self._souradnice

    def hint_clicked(self):
        print(self._souradnice)
        print(self)
        if(Herni_kamen.zvoleny_kamen != None):

            Herni_kamen.presun_kamen(Herni_kamen.zvoleny_kamen, self)
            self._hidden = True

            Herni_kamen.zvoleny_kamen.update_po_presunu(self)
            SoundManager.move_sound.play() # Pustí move.mp3 z soundManageru