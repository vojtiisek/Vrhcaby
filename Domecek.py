import pygame
from tkinter import Canvas, Button

from Zasobnik import Zasobnik
from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu

class Domecek:
    
    domecek_cerny = Zasobnik(15)
    domecek_bily = Zasobnik(15)
    domecky = {"bila" : domecek_bily, 
               "cerna" : domecek_cerny}
    
    #zjistit stav a barvu hrace -> zjistit pozici vybraneho kamene v kvadrantu ktery by mohl do domecku -> spocitat jestli se hod kostky rovná s pozicí kamene -> poslat do domečku
    def presun_do_domecku(self, pozice_kamene : tuple):
        
        mapa_kamenu = Mapa_kamenu._mapa_kamenu
        kamen = None
        for kamen in mapa_kamenu.keys():
            if kamen._pozice_kamene == pozice_kamene:
                break

        if kamen._default_color == "bila":
            Domecek.domecek_bily.push(kamen)
        else:
            Domecek.domecek_cerny.push(kamen)

    def get_pozice(barva : str) -> tuple:
        if(barva == "bila"):
            return (0,1)
        else:
            return (0,2)
