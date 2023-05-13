import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

from Mapa_pozic import Mapa_pozic

class Herni_kamen(tk.Frame):
    def __init__(self, platno, barva_kamene: str, pozice_kamene) -> None: # barva_kamene - bila/cerna/hint/hidden/selected , pozice_kamene - (point, pozice na pointu)
        super().__init__(platno)
        self._barva_kamene = barva_kamene
        self._pozice_kamene = pozice_kamene
        self._historie = []

        if(self._barva_kamene == "bila"):
            self.kamen_bg = Image.open("white_piece.png")
        elif(self._barva_kamene == "cerna"):
            self.kamen_bg = Image.open("black_piece.png")
        elif(self._barva_kamene == "hint"):
            self.kamen_bg = Image.open("hint_piece.png")
        elif(self._barva_kamene == "selected"):
            self.kamen_bg = Image.open("selected_piece.png")
        else:
            self.kamen_bg = Image.open("error_piece.png")

        self.kamen_bg_tk = ImageTk.PhotoImage(self.kamen_bg)
        self.kamen_button= Button(platno, image=self.kamen_bg_tk, command=lambda : Herni_kamen.click_event(self), bd=0, highlightthickness=0)
        self.kamen_button.config(width=self.kamen_bg_tk.width(), height=self.kamen_bg_tk.height())

        mapa = Mapa_pozic._mapa_pozic
        pozice = mapa.get(pozice_kamene)

        platno.create_window(pozice.get_souradnice[0], pozice.get_souradnice[1], window=self.kamen_button)

    @property
    def barva_kamene(self) -> str:
        return self._barva_kamene

    @barva_kamene.setter
    def barva_kamene(self, value):
        self._barva_kamene = value

    @property
    def historie(self) -> list:
        return self._historie

    @property
    def pozice_kamene(self) -> list:
        return self._pozice_kamene

    @pozice_kamene.setter
    def pozice_kamene(self, nova_pozice_kamene: list) -> None:
        if self._pozice_kamene != nova_pozice_kamene:
            self.pridej_pozici_do_historie()
            self._pozice_kamene = nova_pozice_kamene

    def pridej_pozici_do_historie(self) -> None:
        self.historie.append(self.pozice_kamene)

    def __str__(self) -> str:
        return f"Tento {self.barva_kamene} kamen je na pozici {self.pozice_kamene}"

    def click_event(self):
        self.barva_kamene("selected")
