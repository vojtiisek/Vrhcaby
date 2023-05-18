from tkinter import Tk as tk
from tkinter import Canvas, Button

from Zasobnik import Zasobnik
from Mapa_kamenu import Mapa_kamenu

class Bar:
    bar_bily = Zasobnik(15)
    bar_cerny = Zasobnik(15)

    def presun_na_bar(platno : Canvas, pozice_kamene : tuple):
        mapa_kamenu = Mapa_kamenu._mapa_kamenu
        kamen = None
        for kamen in mapa_kamenu.keys():
            if kamen._pozice_kamene == pozice_kamene:
                break

        if kamen._default_color == "bila":
            Bar.bar_bily.push(kamen)
        else:
            Bar.bar_cerny.push(kamen)



