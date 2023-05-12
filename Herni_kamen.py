import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

class Herni_kamen(tk.Frame):
    def __init__(self, platno, barva_kamene: str, pozice_kamene: tuple) -> None: # barva_kamene - bila/cerna/hint/hidden/selected , pozice_kamene - (point, pozice na pointu)
        super().__init__(platno)
        self._barva_kamene = barva_kamene
        self._pozice_kamene = pozice_kamene
        self._historie = []

        if(self.barva_kamene == "bila"):
            kamen_bg = Image.open("white_piece.png")
        elif(self.barva_kamene == "cerna"):
            kamen_bg = Image.open("black_piece.png")
        elif(self.barva_kamene == "hint"):
            kamen_bg = Image.open("hint_piece.png")
        elif(self.barva_kamene == "selected"):
            kamen_bg = Image.open("selected_piece.png")
        else:
            kamen_bg = Image.open("error_piece.png")
        kamen_bg_tk = ImageTk.PhotoImage(kamen_bg)
        kamen_button= Button(platno, image=kamen_bg_tk, command=lambda : ..., bd=0, highlightthickness=0)
        kamen_button.config(width=kamen_bg_tk.width(), height=kamen_bg_tk.height())
        platno.create_window(480, 300, window=kamen_button)

    @property
    def barva_kamene(self) -> str:
        return self._barva_kamene

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
