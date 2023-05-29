from tkinter import Tk as tk
from tkinter import Canvas, messagebox, Button
from PIL import Image, ImageTk
from Label_manager import Label_manager

from Zasobnik import Zasobnik
from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu


class CalculateTahy:

    mozne_tahy = []

    def vyhodnotit_mozne_tahy(platno : Canvas, pozice_kamene : tuple, vysledek_dvojkostky : list) -> list:
        
        CalculateTahy.mozne_tahy = []
        soucet_kostek = vysledek_dvojkostky[0] + vysledek_dvojkostky[1]

        mapa_kamenu = Mapa_kamenu.get_mapa_kamenu()
        kamen = None
        for kamen in mapa_kamenu.keys():
            if kamen._pozice_kamene == pozice_kamene:
                break
        if(kamen._default_color == "bila"):
            if(len(vysledek_dvojkostky) == 2):
                if(CalculateTahy.kontrola_budoucich_mist(pozice_kamene[0], vysledek_dvojkostky, kamen._default_color)):
                   
                    if(CalculateTahy.splnuje_podminky(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]], kamen._default_color)):
                       CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]])
                    if(CalculateTahy.splnuje_podminky(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[1]], kamen._default_color)):
                         CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[1]])

                    if(CalculateTahy.splnuje_podminky(Zasobnik.zasobniky[pozice_kamene[0] - soucet_kostek], kamen._default_color)):
                         CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - soucet_kostek])
            elif(len(vysledek_dvojkostky) == 4):
                if(len(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]]) <=1):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]])
            else:
                messagebox.showinfo("Chyba", f"Chyba pri rozhodovani o velikosti vysledek_dvojkostky, velikost: {len(vysledek_dvojkostky)}"  )
        else:
            if(len(vysledek_dvojkostky) == 2):
                if(CalculateTahy.kontrola_budoucich_mist(pozice_kamene[0], vysledek_dvojkostky, kamen._default_color)):
                    if(CalculateTahy.splnuje_podminky(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]], kamen._default_color)):
                        CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]])

                    if(CalculateTahy.splnuje_podminky(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[1]], kamen._default_color)):
                         CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[1]])

                    if(CalculateTahy.splnuje_podminky(Zasobnik.zasobniky[pozice_kamene[0] + soucet_kostek], kamen._default_color)):
                         CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + soucet_kostek])

            elif(len(vysledek_dvojkostky) == 4):
                if(len(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]].zasobnik) <=1):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]])
            else:
                messagebox.showinfo("Chyba", f"Chyba pri rozhodovani o velikosti vysledek_dvojkostky, velikost: {len(vysledek_dvojkostky)}"  )

        return CalculateTahy.mozne_tahy

    def vykreslit_pozice(seznam_tahu):
        mapa_pozic = Mapa_pozic._mapa_pozic
        for mozny_tah in range(len(seznam_tahu)):
            pozice = None
            vyska = len(seznam_tahu[mozny_tah].zasobnik) + 1
            point = (Zasobnik.zasobniky.index(seznam_tahu[mozny_tah]),vyska)
            pozice = mapa_pozic[point]
            pozice.set_hidden(False)

            print(f"KONEC, pozice: {pozice._souradnice}, point: {point}, mapa pozic: {mapa_pozic[point]._souradnice}")

    def skryj_pozice(platno : Canvas, seznam_tahu):
        mapa_pozic = Mapa_pozic._mapa_pozic
        pozice = None
        for mozny_tah in seznam_tahu:
            vyska = len(mozny_tah.zasobnik) + 1
            point = (Zasobnik.zasobniky.index(mozny_tah),vyska)
            pozice = mapa_pozic[point]
            pozice._hidden = True

            platno.delete("mozny_tah")

    def splnuje_podminky(point_zasobnik : Zasobnik, barva_hrace : str) -> bool:
        vysledek = False

        if(len(point_zasobnik.zasobnik) == 1 and point_zasobnik.rear()._default_color != barva_hrace):
            vysledek = True
        elif(len(point_zasobnik.zasobnik) >= 1 and len(point_zasobnik.zasobnik) <5 and point_zasobnik.rear()._default_color == barva_hrace):
            vysledek = True
        elif(len(point_zasobnik.zasobnik) < 1):
            vysledek = True
        else:
            pass

        return vysledek

    def kontrola_budoucich_mist(pozice_kamene : int, vysledek_dvojkostky : list, barva_hrace : str):
        vysledek = False
        soucet = vysledek_dvojkostky[0] + vysledek_dvojkostky[1]
        if(barva_hrace == "bila"):
            if(pozice_kamene - vysledek_dvojkostky[0] < 1 or pozice_kamene - vysledek_dvojkostky[0] > 24):
                vysledek = False
            else:
                vysledek = True

            if(pozice_kamene - vysledek_dvojkostky[1] < 1 or pozice_kamene - vysledek_dvojkostky[1] > 24):
                vysledek = False
            else:
                vysledek = True

            if(pozice_kamene - soucet < 1 or pozice_kamene - soucet > 24):
                vysledek = False
            else:
                vysledek = True
        else:
            if(pozice_kamene + vysledek_dvojkostky[0] < 1 or pozice_kamene + vysledek_dvojkostky[0] > 24):
                vysledek = False
            else:
                vysledek = True

            if(pozice_kamene + vysledek_dvojkostky[1] < 1 or pozice_kamene + vysledek_dvojkostky[1] > 24):
                vysledek = False
            else:
                vysledek = True

            if(pozice_kamene + soucet < 1 or pozice_kamene + soucet > 24):
                vysledek = False
            else:
                vysledek = True
        return vysledek