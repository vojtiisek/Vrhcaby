import pygame
from tkinter import Canvas, Button
from Dvojkostka import Dvojkostka
from StavHry import StavHry

from Zasobnik import Zasobnik
from Mapa_kamenu import Mapa_kamenu

class Domecek:
    
    stav_hry = StavHry.get_stav()
    #zjistit stav a barvu hrace -> zjistit pozici vybraneho kamene ktery by mohl do domecku ->spocitat jestli se hod kostky rovná s pozicí kamene -> poslat do domečku
    def presun_do_domecku(platno : Canvas, pozice_kamene : tuple):
        mapa_kamenu = Mapa_kamenu.get_mapa_kamenu()
        print(mapa_kamenu)
        
        
        