import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

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

            #mapa_pozic = Mapa_pozic._mapa_pozic
            #nova_pozice = mapa_pozic[Herni_kamen.zvoleny_kamen._pozice_kamene] #pozice kamene pred presunem (misto nej se vytvori volna Pozice())
            Herni_kamen.presun_kamen(Herni_kamen.zvoleny_kamen, self)
            self._hidden = True
            Herni_kamen.zvoleny_kamen._platno.delete("selected")

            #nova_pozice.pozice_bg = Image.open("hint_piece.png") 
            #nova_pozice.pozice_bg_tk = ImageTk.PhotoImage(nova_pozice.pozice_bg)
            #nova_pozice.kamen_button= Button(nova_pozice._platno, image=nova_pozice.pozice_bg_tk, command=lambda : Pozice.hint_clicked(nova_pozice), bd=0, highlightthickness=0)
            #nova_pozice.kamen_button.config(width=nova_pozice.pozice_bg_tk.width(), height=nova_pozice.pozice_bg_tk.height())
            #nova_pozice._platno.create_window(nova_pozice._souradnice[0], nova_pozice._souradnice[1], window=nova_pozice.kamen_button)

            Herni_kamen.zvoleny_kamen.update_po_presunu(self)