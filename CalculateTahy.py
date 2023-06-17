from tkinter import Tk as tk
from tkinter import Canvas, messagebox, Button
from PIL import Image, ImageTk
from Label_manager import Label_manager

from Zasobnik import Zasobnik
from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu
from StavHry import StavHry
from Domecek import Domecek


class CalculateTahy:

    mozne_tahy = []
    vysledne_zasobniky_bily = [] # na jake pointy (zasobniky) muze hrac dane barvy se zvolenym kamenem jit dle hozenych cisel z Dvojkostky. Nejsou upraveny pravidly.
    vysledne_zasobniky_cerny = [] # Musi se projet, zkontrolovat, zda splnuji podminky a pravidla a az pak pridat jakozto mozny tah.

    hrac = None

    def vyhodnotit_mozne_tahy(platno : Canvas, pozice_kamene : tuple, vysledek_dvojkostky : list) -> list: 
        print("vyhodnocuji tahy")
        CalculateTahy.mozne_tahy = []
        CalculateTahy.vysledne_zasobniky_bily.clear()
        CalculateTahy.vysledne_zasobniky_cerny.clear()

        hraci = StavHry.get_hraci()
        hrac = hraci[StavHry.get_stav()]
        velikost_hodu = hrac.get_hozeny_pocet

        mapa_kamenu = Mapa_kamenu.get_mapa_kamenu()
        kamen = None
        for kamen in mapa_kamenu.keys():
            if kamen._pozice_kamene == pozice_kamene:
                break

        print(f"pozice kamene pred: {pozice_kamene}")
        print(f"barva: {kamen._default_color}")
        if(pozice_kamene[0] == 99):
            if(kamen._default_color == "bila"):
                pozice_kamene = (0,0)
            else:
                pozice_kamene = (25,0)

        print(f"pozice_kamene po: {pozice_kamene}")
        print(f"vysledek_dvojkostky: {vysledek_dvojkostky}")
        if(len(vysledek_dvojkostky) == 4 or len(vysledek_dvojkostky) == 3): 
            CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] + vysledek_dvojkostky[0])

            CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] - vysledek_dvojkostky[0])                   
            
        elif(len(vysledek_dvojkostky) == 2):
            if(velikost_hodu != 4):
                CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] + vysledek_dvojkostky[0])
                CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] + vysledek_dvojkostky[1])


                CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] - vysledek_dvojkostky[0])
                CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] - vysledek_dvojkostky[1])
            else:
                CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] + vysledek_dvojkostky[0])

                CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] - vysledek_dvojkostky[0])   

        elif(len(vysledek_dvojkostky) == 1):
            if(velikost_hodu != 4):
                CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] + vysledek_dvojkostky[0])

                CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] - vysledek_dvojkostky[0])
            else:
                CalculateTahy.vysledne_zasobniky_bily.append(pozice_kamene[0] + vysledek_dvojkostky[0])

                CalculateTahy.vysledne_zasobniky_cerny.append(pozice_kamene[0] - vysledek_dvojkostky[0])   
        else:
             messagebox.showinfo("Chyba", f"Chyba pri rozhodovani o vyslednych zasobnicich, velikost vysledek_dvojkostky: {len(vysledek_dvojkostky)}"  )


        #mapa_kamenu = Mapa_kamenu.get_mapa_kamenu()
        #kamen = None
        #for kamen in mapa_kamenu.keys():
        #    if kamen._pozice_kamene == pozice_kamene:
        #        break


        CalculateTahy.kontrola_budoucich_mist()
        CalculateTahy.splnuje_podminky(kamen._default_color)

        print("vyhodnoceno")
        return CalculateTahy.mozne_tahy

    def vykreslit_pozice(seznam_tahu):
        mapa_pozic = Mapa_pozic._mapa_pozic
        for mozny_tah in range(len(seznam_tahu)):
            if(seznam_tahu[mozny_tah] == Domecek.domecek_bily):
                pozice = mapa_pozic[(0,2)]
                pozice.set_hidden(False)
            elif(seznam_tahu[mozny_tah] == Domecek.domecek_cerny):
                pozice = mapa_pozic[(0,1)]
                pozice.set_hidden(False)
            else:
                pozice = None
                vyska = len(seznam_tahu[mozny_tah].zasobnik) + 1
                point = (Zasobnik.zasobniky.index(seznam_tahu[mozny_tah]),vyska)
                pozice = mapa_pozic[point]
                pozice.set_hidden(False)

    def skryj_pozice(platno : Canvas, seznam_tahu):
        mapa_pozic = Mapa_pozic._mapa_pozic
        pozice = None
        for mozny_tah in seznam_tahu:
            if(mozny_tah == Domecek.domecek_bily):
                pozice = mapa_pozic[(0,2)]
                pozice._hidden = True
            elif(mozny_tah == Domecek.domecek_cerny):
                pozice = mapa_pozic[(0,1)]
                pozice._hidden = True
            else:
                vyska = len(mozny_tah.zasobnik) + 1
                point = (Zasobnik.zasobniky.index(mozny_tah),vyska)
                pozice = mapa_pozic[point]
                pozice._hidden = True

            platno.delete("mozny_tah")

    def splnuje_podminky(barva_hrace : str) -> None:
        if(barva_hrace == "bila"):
            for zasobnik in CalculateTahy.vysledne_zasobniky_bily:
                print(f"Zasobnik ve for: {zasobnik}")
                if(zasobnik == 25):
                    CalculateTahy.mozne_tahy.append(Domecek.domecek_bily)
                else:
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
                if(zasobnik == 0):
                    CalculateTahy.mozne_tahy.append(Domecek.domecek_cerny)
                else:
                    if(len(Zasobnik.zasobniky[zasobnik].zasobnik) == 1 and Zasobnik.zasobniky[zasobnik].rear()._default_color != barva_hrace):
                        CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                    elif(len(Zasobnik.zasobniky[zasobnik].zasobnik) >= 1 and len(Zasobnik.zasobniky[zasobnik].zasobnik) <5 and Zasobnik.zasobniky[zasobnik].rear()._default_color == barva_hrace):
                        CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                    elif(len(Zasobnik.zasobniky[zasobnik].zasobnik) < 1):
                        CalculateTahy.mozne_tahy.append(Zasobnik.zasobniky[zasobnik])
                    else:
                        pass
        print(f"Splnuje podminky: {CalculateTahy.mozne_tahy}")


    def kontrola_budoucich_mist():
        if(len(CalculateTahy.vysledne_zasobniky_bily) > 0):
            for point in CalculateTahy.vysledne_zasobniky_bily:
                if(point < 1 or point > 25):
                    print(f"Odstranuji v kontrole BILY: {point}")
                    CalculateTahy.vysledne_zasobniky_bily.remove(point)

        if(len(CalculateTahy.vysledne_zasobniky_cerny) > 0):
            for point in CalculateTahy.vysledne_zasobniky_cerny:
                if(point < 0 or point > 24):
                    print(f"Odstranuji v kontrole CERNY: {point}")
                    CalculateTahy.vysledne_zasobniky_cerny.remove(point)