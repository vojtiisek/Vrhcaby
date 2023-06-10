from tkinter import Canvas

from Zasobnik import Zasobnik
from Mapa_kamenu import Mapa_kamenu

class Bar:
    bar_bily = Zasobnik(15)
    bar_cerny = Zasobnik(15)
    
    bary = {"bila":bar_bily, "cerna":bar_cerny}

    def get_bary(barva : str):
        if(barva == "bila" or barva == "cerna"):
            return Bar.bary[barva]

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

    def presun_z_baru(pozice_kamene : tuple):
        mapa_kamenu = Mapa_kamenu._mapa_kamenu
        kamen = None
        for kamen in mapa_kamenu.keys():
            if kamen._pozice_kamene == pozice_kamene:
                break

        if kamen._default_color == "bila":
            Bar.bar_bily.pop()
        else:
            Bar.bar_cerny.pop()



