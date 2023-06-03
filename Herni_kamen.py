from ast import If
import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path
from CalculateTahy import CalculateTahy

from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu
from Zasobnik import Zasobnik
from Label_manager import Label_manager
from Bar import Bar
from StavHry import StavHry
from Domecek import Domecek

class Herni_kamen(tk.Frame):
    zvoleny_kamen = None
    barva_hrace = None
    posledni_vysledky_hodu = []
    def __init__(self, platno, barva_kamene: str, pozice_kamene: tuple, historie: list) -> None: # barva_kamene - bila/cerna/hint/hidden/selected , pozice_kamene - (point, pozice na pointu)
        super().__init__(platno)
        self._platno = platno
        self._barva_kamene = barva_kamene
        self._pozice_kamene = pozice_kamene
        self._tag = "tag" + str(self._pozice_kamene[0]) + str(self._pozice_kamene[1])
        self._historie = historie
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
        pozice = mapa.get(self._pozice_kamene)

        platno.create_window(pozice.get_souradnice[0], pozice.get_souradnice[1], window=self.kamen_button, tags=self._tag)

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
    def pozice_kamene(self) -> tuple:
        return self._pozice_kamene

    @pozice_kamene.setter
    def pozice_kamene(self, nova_pozice_kamene: tuple) -> None:
        if self._pozice_kamene != nova_pozice_kamene:
            self.pridej_pozici_do_historie()
            self._pozice_kamene = nova_pozice_kamene

    def pridej_pozici_do_historie(self) -> None:
        #print(f"POZICE KAMENE {self._pozice_kamene}")
        #print(f"HISTORIE {self._historie}")
        if(self._pozice_kamene != (99,1) or self._pozice_kamene != (99,2)): 
            self._historie.append(self._pozice_kamene)
        else:
            self._historie.append("Bar")

    def __str__(self) -> str:
        return f"Tento {self.barva_kamene} kamen je na pozici {self.pozice_kamene}"

    def click_event(self):
        print(f"Self: {self._pozice_kamene}")
        hraci = StavHry.get_hraci()
        if(StavHry.get_stav() == "Hrac1" or StavHry.get_stav() == "Hrac2"):
            if(self._default_color.__eq__(hraci[StavHry.get_stav()].get_barva)):
                if Herni_kamen.zvoleny_kamen == None or Herni_kamen.zvoleny_kamen == self:
                    if(Zasobnik.zasobniky[self._pozice_kamene[0]].rear() == self):        
                        if(len(hraci[StavHry.get_stav()].get_vysledky) > 0 ) :
                            if(hraci[StavHry.get_stav()].get_hozeny_pocet == 4 and self in hraci[StavHry.get_stav()].get_odehrane_kameny):
                                messagebox.showinfo("Informace", "Musite hrat se ctyrmi ruznymi kameny, jelikoz jste hodili dve stejna cisla.")
                            elif(((hraci[StavHry.get_stav()].get_hozeny_pocet == 4 and self not in hraci[StavHry.get_stav()].get_odehrane_kameny) 
                                  or hraci[StavHry.get_stav()].get_hozeny_pocet == 2)):
                                
                                mozne_tahy = CalculateTahy.vyhodnotit_mozne_tahy(self._platno, self._pozice_kamene, hraci[StavHry.get_stav()].get_vysledky)

                                if(self._barva_kamene == "bila" or self._barva_kamene == "cerna"):
                        
                                    CalculateTahy.vykreslit_pozice(mozne_tahy)
                                    self._barva_kamene = "selected"

                                    self.kamen_bg = Image.open("selected_piece.png")
                                    Herni_kamen.zvoleny_kamen = self

                                elif(self._barva_kamene == "selected"):



                                    CalculateTahy.skryj_pozice(self._platno, mozne_tahy)
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
                                pozice = mapa.get(self._pozice_kamene)

                                self._platno.create_window(pozice.get_souradnice[0], pozice.get_souradnice[1], window=self.kamen_button, tags=self._tag)
                        else:
                            messagebox.showinfo("Upozorneni", "Musite si nejdrive hodit kostkami!")
                    else:
                        messagebox.showinfo("Informace", "Muzete hrat pouze s nejvyse umistenym kamenem na danem klinu.")
                else:
                    messagebox.showinfo("Informace", "Jiz mate vybrany jiny kamen, se kterym chcete hybat.")
            
    def update_po_presunu(self, nova_pozice):
        self._barva_kamene = self._default_color
        mapa_pozic = Mapa_pozic._mapa_pozic
        mapa_kamenu = Mapa_kamenu._mapa_kamenu

        nova_pozice = mapa_kamenu[self]

        point = ()
        for point in mapa_pozic.keys():
            if mapa_pozic[point] == nova_pozice:
                break

        if(point == (99,1) or point == (99,2)):
            ...
        else:
            if(Zasobnik.zasobniky[point[0]] in CalculateTahy.mozne_tahy) :
                CalculateTahy.mozne_tahy.remove(Zasobnik.zasobniky[point[0]])

        CalculateTahy.skryj_pozice(self._platno, CalculateTahy.mozne_tahy)
        Herni_kamen.zvoleny_kamen = None

        if(self._default_color == "bila"):
            self.kamen_bg = Image.open("white_piece.png")
        elif(self._default_color == "cerna"):
            self.kamen_bg = Image.open("black_piece.png")
        else:
            self.kamen_bg = Image.open("error_piece.png")

        if(nova_pozice != mapa_pozic[(0,1)] and nova_pozice != mapa_pozic[(0,2)]):
            self.kamen_bg_tk = ImageTk.PhotoImage(self.kamen_bg)
            self.kamen_button= Button(self._platno, image=self.kamen_bg_tk, command=lambda : Herni_kamen.click_event(self), bd=0, highlightthickness=0)
            self.kamen_button.config(width=self.kamen_bg_tk.width(), height=self.kamen_bg_tk.height())
            self._platno.create_window(nova_pozice.get_souradnice[0], nova_pozice.get_souradnice[1], window=self.kamen_button, tags=self._tag) 

        hraci = StavHry.get_hraci()

        hraci[StavHry.get_stav()].get_odehrane_kameny.append(self)
        print(f"Odehrane kameny: {hraci[StavHry.get_stav()].get_odehrane_kameny}")
        if(len(hraci[StavHry.get_stav()].get_vysledky) < 1):
            hraci["Hrac1"].get_odehrane_kameny.clear()
            hraci["Hrac2"].get_odehrane_kameny.clear()
            if(StavHry.get_stav() == "Hrac1"):
                print("zmena na hrace2")
                StavHry.set_stav("Hrac2")
            else:
                print("zmena na hrace1")
                StavHry.set_stav("Hrac1")      

        #print(f"{self.historie[-2], self.historie[-1]}")
        #print(f"HISTORIE PŘED VYPSÁNÍM: {self._historie}")
        Label_manager.zmena_stavu(self._platno, "",f"{StavHry.get_stav()} hraje ({hraci[StavHry.get_stav()].get_barva}). Hodte si dvojkostkou!")
        Label_manager.zmena_pozice(self._platno,self._default_color, self.historie[-2], self._historie[-1], None)

    def presun_kamen(kamen, nova_pozice):
        hraci = StavHry.get_hraci()
        puvodni_pozice = kamen._pozice_kamene
        
        kamen._platno.delete(kamen._tag)
        Zasobnik.zasobniky[kamen._pozice_kamene[0]].pop()
        mapa_pozic = Mapa_pozic._mapa_pozic
        mapa_kamenu = Mapa_kamenu._mapa_kamenu

        point = ()
        for point in mapa_pozic.keys():
            if mapa_pozic[point] == nova_pozice:
                break

        if(point == (99,1) or point == (99,2)): 
            ...
        elif(point == (0,1) or point == (0,2)):
            if(kamen._default_color == "bila"):
                Domecek.domecek_bily.push(kamen)
            else:
                Domecek.domecek_cerny.push(kamen)

            vzdalenost = Herni_kamen.vypocitej_vzdalenost(kamen._default_color, puvodni_pozice[0], point[0])
            if(vzdalenost in hraci[StavHry.get_stav()].get_vysledky):
                hraci[StavHry.get_stav()].get_vysledky.remove(vzdalenost)
            else:
                hraci[StavHry.get_stav()].get_vysledky.clear()
        else:
            print(f"Point: {point}")
            if(len(Zasobnik.zasobniky[point[0]].zasobnik) == 1):
                if(Zasobnik.zasobniky[point[0]].rear()._default_color != kamen._default_color):
                    vyhozeny_kamen = Zasobnik.zasobniky[point[0]].rear()
                    point = vyhozeny_kamen._pozice_kamene
                    nova_pozice = mapa_kamenu[vyhozeny_kamen]
                    Zasobnik.zasobniky[point[0]].pop()
                    Herni_kamen.vyhodit_na_bar(vyhozeny_kamen)
            Zasobnik.zasobniky[point[0]].push(kamen)
            vzdalenost = Herni_kamen.vypocitej_vzdalenost(kamen._default_color, puvodni_pozice[0], point[0])
            if(vzdalenost in hraci[StavHry.get_stav()].get_vysledky):
                hraci[StavHry.get_stav()].get_vysledky.remove(vzdalenost)
            else:
                hraci[StavHry.get_stav()].get_vysledky.clear()

        kamen._pozice_kamene = point
        kamen.pridej_pozici_do_historie()

        mapa_kamenu[kamen] = nova_pozice
        Herni_kamen.zvoleny_kamen = kamen

    def vyhodit_na_bar(self):
        mapa_pozic = Mapa_pozic._mapa_pozic
        Bar.presun_na_bar(self._platno, self._pozice_kamene)
        if(self._default_color == "bila"):
            Herni_kamen.presun_kamen(self, mapa_pozic[(99,1)])    
            self.update_po_presunu(mapa_pozic[(99,1)])
        else:
            Herni_kamen.presun_kamen(self, mapa_pozic[(99,2)])    
            self.update_po_presunu(mapa_pozic[(99,2)])

    def vypocitej_vzdalenost(barva : str, puvodni_pozice : tuple, nova_pozice : tuple) -> int:
        if(barva == "cerna"):
            return (puvodni_pozice - nova_pozice)
        else:
            return (nova_pozice - puvodni_pozice)