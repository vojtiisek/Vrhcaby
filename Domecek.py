import pygame
from tkinter import Canvas, Button
from Dvojkostka import Dvojkostka
from StavHry import StavHry

from Zasobnik import Zasobnik
from Mapa_pozic import Mapa_pozic
from Herni_kamen import Herni_kamen
from Mapa_kamenu import Mapa_kamenu

class Domecek:
    
    domecek_cerny = Zasobnik(15)
    domecek_bily = Zasobnik(15)
    
    
    stav_hry = StavHry.get_stav()
    hrac = stav_hry[StavHry.get_stav()]
    #zjistit stav a barvu hrace -> zjistit pozici vybraneho kamene v kvadrantu ktery by mohl do domecku -> spocitat jestli se hod kostky rovná s pozicí kamene -> poslat do domečku
    def presun_do_domecku(self, pozice_kamene : tuple, vysledek_dvojkostky : list):
        
        mapa_pozic = Mapa_pozic.get_mapa_pozic().keys()
        if(StavHry.get_stav() == "Hrac1" or StavHry.get_stav() == "Hrac2"):
            for zasobnik in Zasobnik: #projeti kazdeho spiku 
                if not zasobnik.is_empty(): #zjisteni jestli spike je prazdny a nema zadne kameny
                    #zjistit jak kontrolovat spiky pres point a porovnat to s zasobnikem
                    if(Herni_kamen.barva_hrace == "bila"):
                        if (Herni_kamen.zvoleny_kamen == None or Herni_kamen.zvoleny_kamen == self):
                            #cerna je posledni kvadrant 19-24 X bila je kvadrant 6-1
                            if 6 <= Herni_kamen.zvoleny_kamen.pozice_kamene[0] >= 1:
                                print("Halda testuju: " + mapa_pozic)
                            elif 24 <= Herni_kamen.zvoleny_kamen.pozice_kamene[0] >= 19:
                                pass
                        #if(len(vysledek_dvojkostky) == pozice vybraneho kamene s danou barvou v poslednim kvadrantu):