from tkinter import Tk as tk
from tkinter import Canvas, messagebox

from Zasobnik import Zasobnik
from Pozice import Pozice
from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu


class CalculateTahy:

    # Bude se vyvolavat drive nez nastaveni zvoleneho_kamene v Herni_kamen. Bude vracet seznam pozic, na ktere se muze presunout.
    # Do click_event Kamene se prida nasledujici funkce. Jakmile je barva_kamene == suggested (nebo zvoleny_kamen == self), pak se vykresli Pozice(), ktere tato funkce vyplivla.
    # Pokud se na kamen klikne znovu, tedy se odznaci, volne Pozice() se skryji. Seznam volnych tahu se smaze pri naslednem vyhodnocovani volnych tahu.
    def vyhodnotit_mozne_tahy(platno : Canvas, pozice_kamene : tuple, vysledek_dvojkostky : list) -> list:
        mozne_tahy = []
        
        mapa_kamenu = Mapa_kamenu._mapa_kamenu
        kamen = None
        for kamen in mapa_kamenu.keys():
            if kamen._pozice_kamene == pozice_kamene:
                break

        if(kamen._default_color == "bila"):
            if(len(vysledek_dvojkostky) == 2):
                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]].zasobnik) >=2)):
                   mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]])

                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[1]].zasobnik) >=2)):
                    mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[1]])

                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] - (vysledek_dvojkostky[0] + vysledek_dvojkostky[1])].zasobnik) >=2)):
                    mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - (vysledek_dvojkostky[0] + vysledek_dvojkostky[1])])

            elif(len(vysledek_dvojkostky) == 4):
                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]].zasobnik) >=2)):
                   mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] - vysledek_dvojkostky[0]])
            else:
                messagebox.showinfo("Chyba", f"Chyba pri rozhodovani o velikost vysledek_dvojkostky, velikost: {len(vysledek_dvojkostky)}"  )
        else:
            if(len(vysledek_dvojkostky) == 2):
                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]].zasobnik) >=2)):
                   mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]])

                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[1]].zasobnik) >=2)):
                    mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[1]])

                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] + (vysledek_dvojkostky[0] + vysledek_dvojkostky[1])].zasobnik) >=2)):
                    mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + (vysledek_dvojkostky[0] + vysledek_dvojkostky[1])])

            elif(len(vysledek_dvojkostky) == 4):
                if(not(len(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]].zasobnik) >=2)):
                   mozne_tahy.append(Zasobnik.zasobniky[pozice_kamene[0] + vysledek_dvojkostky[0]])
                ...
            else:
                messagebox.showinfo("Chyba", f"Chyba pri rozhodovani o velikost vysledek_dvojkostky, velikost: {len(vysledek_dvojkostky)}"  )

