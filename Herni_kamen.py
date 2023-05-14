import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu
from Zasobnik import Zasobnik

class Herni_kamen(tk.Frame):
    zvoleny_kamen = None
    barva_hrace = None
    def __init__(self, platno, barva_kamene: str, pozice_kamene) -> None: # barva_kamene - bila/cerna/hint/hidden/selected , pozice_kamene - (point, pozice na pointu)
        super().__init__(platno)
        self._platno = platno
        self._barva_kamene = barva_kamene
        self._pozice_kamene = pozice_kamene
        self._historie = []
        self._default_color = barva_kamene

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
    def set_barva_kamene(self, value):
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
        if(self._default_color == Herni_kamen.barva_hrace):
            if Herni_kamen.zvoleny_kamen == None or Herni_kamen.zvoleny_kamen == self:
                if(Zasobnik.zasobniky[self.pozice_kamene[0]].rear() == self):
            
                    if(self._barva_kamene == "bila" or self._barva_kamene == "cerna"):

                        self._barva_kamene = "selected"
                        self.kamen_bg = Image.open("selected_piece.png")
                        Herni_kamen.zvoleny_kamen = self

                    elif(self._barva_kamene == "selected"):

                        self._barva_kamene = self._default_color
                        Herni_kamen.zvoleny_kamen = None

                        if(self._default_color == "bila"):
                            self.kamen_bg = Image.open("white_piece.png")
                        elif(self._default_color == "cerna"):
                            self.kamen_bg = Image.open("black_piece.png")
                        else:
                            self.kamen_bg = Image.open("error_piece.png")
                    else:
                        self.kamen_bg = Image.open("error_piece.png")

                    self.kamen_bg_tk = ImageTk.PhotoImage(self.kamen_bg)
                    self.kamen_button= Button(self._platno, image=self.kamen_bg_tk, command=lambda : Herni_kamen.click_event(self), bd=0, highlightthickness=0)
                    self.kamen_button.config(width=self.kamen_bg_tk.width(), height=self.kamen_bg_tk.height())

                    mapa = Mapa_pozic._mapa_pozic
                    pozice = mapa.get(self.pozice_kamene)

                    self._platno.create_window(pozice.get_souradnice[0], pozice.get_souradnice[1], window=self.kamen_button)
                else:
                    messagebox.showinfo("Informace", "Muzete hrat pouze s nejvyse umistenym kamenem na danem klinu.")
            else:
                messagebox.showinfo("Informace", "Jiz mate vybrany jiny kamen, se kterym chcete hybat.")

    def update_po_presunu(self, nova_pozice):
        self._platno.delete(self)
        if(self._barva_kamene == "bila" or self._barva_kamene == "cerna"):
            self._barva_kamene = "selected"
            self.kamen_bg = Image.open("selected_piece.png")
            Herni_kamen.zvoleny_kamen = self 
            #self.platno.update()

        elif(self._barva_kamene == "selected"):

            self._barva_kamene = self._default_color
            Herni_kamen.zvoleny_kamen = None

            if(self._default_color == "bila"):
                self.kamen_bg = Image.open("white_piece.png")
            elif(self._default_color == "cerna"):
                self.kamen_bg = Image.open("black_piece.png")
            else:
                self.kamen_bg = Image.open("error_piece.png")
        else:
            self.kamen_bg = Image.open("error_piece.png")

        self.kamen_bg_tk = ImageTk.PhotoImage(self.kamen_bg)
        self.kamen_button= Button(self._platno, image=self.kamen_bg_tk, command=lambda : Herni_kamen.click_event(self), bd=0, highlightthickness=0)
        self.kamen_button.config(width=self.kamen_bg_tk.width(), height=self.kamen_bg_tk.height())
        self._platno.create_window(nova_pozice.get_souradnice[0], nova_pozice.get_souradnice[1], window=self.kamen_button) 

    def presun_kamen(kamen, nova_pozice):
        Zasobnik.zasobniky[kamen._pozice_kamene[0]].pop()
        mapa_pozic = Mapa_pozic._mapa_pozic
        point = ()
        for point in mapa_pozic.keys():
            if mapa_pozic[point] == nova_pozice:
                print(f"Nalezeny point: {point}")
                break
        Zasobnik.zasobniky[point[0]].push(kamen)
        mapa_kamenu = Mapa_kamenu._mapa_kamenu
        mapa_kamenu[kamen] = nova_pozice
        