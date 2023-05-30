from tkinter import Tk as tk
from tkinter import Canvas, messagebox, Button
from PIL import Image, ImageTk
from Label_manager import Label_manager

from Zasobnik import Zasobnik
from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu


class CalculateTahy:

    mozne_tahy = []
    vysledne_zasobniky_bily = [] # na jake pointy (zasobniky) muze hrac dane barvy se zvolenym kamenem jit dle hozenych cisel z Dvojkostky. Nejsou upraveny pravidly.
    vysledne_zasobniky_cerny = [] # Musi se projet, zkontrolovat, zda splnuji podminky a pravidla a az pak pridat jakozto mozny tah.

    def vyhodnotit_mozne_tahy(platno : Canvas, pozice_kamene : tuple, vysledek_dvojkostky : list) -> list: 
        
        CalculateTahy.mozne_tahy = []
        CalculateTahy.vysledne_zasobniky_bily.clear()
        CalculateTahy.vysledne_zasobniky_cerny.clear()

        if(len(vysledek_dvojkostky) == 4): # aby nedoslo k tomu, ze se od len 2 povoli hybani s ostatnimi kostkami, tak musim do Hrace pridat posledne hozeny pocet tahu, ktery bude nemenny, 
            ...                            # dokud nespotrebuje vsechny 4 tahy
        elif(len(vysledek_dvojkostky) == 3): 
            ...
        elif(len(vysledek_dvojkostky) == 2):
            CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] - vysledek_dvojkostky[0])
            CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] - vysledek_dvojkostky[1])
            CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] - (vysledek_dvojkostky[1] + vysledek_dvojkostky[1]))

            CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] + vysledek_dvojkostky[0])
            CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] + vysledek_dvojkostky[1])
            CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] + (vysledek_dvojkostky[1] + vysledek_dvojkostky[1]))

        elif(len(vysledek_dvojkostky) == 1):
            CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] - vysledek_dvojkostky[0])

            CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] + vysledek_dvojkostky[0])
        else:
             messagebox.showinfo("Chyba", f"Chyba pri rozhodovani o vyslednych zasobnicich, velikost vysledek_dvojkostky: {len(vysledek_dvojkostky)}"  )


        mapa_kamenu = Mapa_kamenu.get_mapa_kamenu()
        kamen = None
        for kamen in mapa_kamenu.keys():
            if kamen._pozice_kamene == pozice_kamene:
                break


        CalculateTahy.kontrola_budoucich_mist(kamen._default_color)
        CalculateTahy.splnuje_podminky(kamen._default_color)

        return CalculateTahy.mozne_tahy

    def vykreslit_pozice(seznam_tahu):
        mapa_pozic = Mapa_pozic._mapa_pozic
        for mozny_tah in range(len(seznam_tahu)):
            pozice = None
            vyska = len(seznam_tahu[mozny_tah].zasobnik) + 1
            point = (Zasobnik.zasobniky.index(seznam_tahu[mozny_tah]),vyska)
            pozice = mapa_pozic[point]
            pozice.set_hidden(False)

    def skryj_pozice(platno : Canvas, seznam_tahu):
        mapa_pozic = Mapa_pozic._mapa_pozic
        pozice = None
        for mozny_tah in seznam_tahu:
            vyska = len(mozny_tah.zasobnik) + 1
            point = (Zasobnik.zasobniky.index(mozny_tah),vyska)
            pozice = mapa_pozic[point]
            pozice._hidden = True

            platno.delete("mozny_tah")

    def splnuje_podminky(barva_hrace : str) -> None:
        if(barva_hrace == "bila"):
            for zasobnik in CalculateTahy.vysledne_zasobniky_bily:
                if(len(Zasobnik.zasobniky[zasobnik].zasobnik) == 1 and Zasobnik.zasobniky[zasobnik].rear()._default_color != barva_hrace):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                elif(len(Zasobnik.zasobniky[zasobnik].zasobnik) >= 1 and len(Zasobnik.zasobniky[zasobnik].zasobnik) <5 and Zasobnik.zasobniky[zasobnik].rear()._default_color == barva_hrace):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                elif(len(Zasobnik.zasobniky[zasobnik].zasobnik) < 1):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                else:
                    pass
        else:
            for zasobnik in CalculateTahy.vysledne_zasobniky_cerny:
                if(len(Zasobnik.zasobniky[zasobnik].zasobnik) == 1 and Zasobnik.zasobniky[zasobnik].rear()._default_color != barva_hrace):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                elif(len(Zasobnik.zasobniky[zasobnik].zasobnik) >= 1 and len(Zasobnik.zasobniky[zasobnik].zasobnik) <5 and Zasobnik.zasobniky[zasobnik].rear()._default_color == barva_hrace):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                elif(len(Zasobnik.zasobniky[zasobnik].zasobnik) < 1):
                    CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                else:
                    pass


    def kontrola_budoucich_mist(barva_hrace : str):
        if(barva_hrace == "bila"):
            for point in CalculateTahy.vysledne_zasobniky_bily:
                if(point < 1 or point > 24):
                    CalculateTahy.vysledne_zasobniky_bily.remove(point)
        else:
            for point in CalculateTahy.vysledne_zasobniky_cerny:
                if(point < 1 or point > 24):
                    CalculateTahy.vysledne_zasobniky_cerny.remove(point)