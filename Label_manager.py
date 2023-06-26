from tkinter import Tk as tk
from tkinter import Label, Canvas
import textwrap

from StavHry import StavHry
from Domecek import Domecek

class Label_manager:

    dvojkostka_labely = {}

    def zmena_pozice(platno : Canvas, barva : str, z_pozice : tuple, na_pozici: tuple, sebrany_kamen : tuple) -> None:
        z_pozice_processed = z_pozice
        na_pozici_processed = na_pozici

        if(z_pozice == (99,1)):
            z_pozice_processed = "Bar"

        if(na_pozici == (99,1)):
            na_pozici_processed = "Bar"


        if(z_pozice == (99,2)):
            z_pozice_processed = "Bar"

        if(na_pozici == (99,2)):
            na_pozici_processed = "Bar"

        if(na_pozici == (0,1)):
            na_pozici_processed = "Domecek"

        if(na_pozici == (0,2)):
            na_pozici_processed = "Domecek"


        if(barva == "bila"):

            posledni_tah_bila_lbl = Label(platno, text=f"{z_pozice_processed} -> {na_pozici_processed}")
            posledni_tah_bila_lbl.config(font=("Arial", 16), fg="white", bg="#843c24")
            posledni_tah_bila_lbl.place(x=701, y=50)
        else: # barva = "cerna"
            posledni_tah_cerna_lbl = Label(platno, text=f"{z_pozice_processed} -> {na_pozici_processed}")
            posledni_tah_cerna_lbl.config(font=("Arial", 16), fg="white", bg="#843c24")
            posledni_tah_cerna_lbl.place(x=701, y=125)

    def zmena_stavu(platno : Canvas, barva : str, stav : str) -> None:
        aktualni_stav_hry_lbl = Label(platno)
        aktualni_stav_hry_lbl.config(text=textwrap.fill(stav, 25), font=("Arial", 16), fg="white", bg="#843c24") 
        aktualni_stav_hry_lbl.place(x=705, y=235)
        aktualni_stav_hry_lbl.update()

    def zobraz_vysledky_dvojkostky(platno : Canvas, barva : str, vysledek : list):
        nick = ""
        if barva == "bila":
            nick = "Bily"
        else:
            nick = "Cerny"

        if(StavHry.get_stav() == "Hrac1" or StavHry.get_stav() == "Hrac2"):
            if("bila" in Label_manager.dvojkostka_labely):
                Label_manager.dvojkostka_labely["bila"].destroy()
            if("cerna" in Label_manager.dvojkostka_labely):
                Label_manager.dvojkostka_labely["cerna"].destroy()

        text = f"{nick} hodil: "
        if(len(vysledek) > 0):
            for cislo in vysledek:
                text = text + str(cislo) + "; "

            if(barva == "bila"):

                vysledek_dvojkostky_bila_lbl = Label(platno, text=text)
                vysledek_dvojkostky_bila_lbl.config(font=("Arial", 16), fg="white", bg="#843c24")
                vysledek_dvojkostky_bila_lbl.place(x=50, y=300)
                Label_manager.dvojkostka_labely["bila"] = vysledek_dvojkostky_bila_lbl
            else:
                vysledek_dvojkostky_cerna_lbl = Label(platno, text=text)
                vysledek_dvojkostky_cerna_lbl.config(font=("Arial", 16), fg="white", bg="#843c24")
                vysledek_dvojkostky_cerna_lbl.place(x=400, y=300)
                Label_manager.dvojkostka_labely["cerna"] = vysledek_dvojkostky_cerna_lbl
        else:
            if(barva == "bila"):
                Label_manager.dvojkostka_labely["bila"].destroy()
            else:
                Label_manager.dvojkostka_labely["cerna"].destroy()


    def update_domecku(platno : Canvas, barva : str):
        hraci = StavHry.get_hraci()
        hrac_dle_barvy = hraci["Hrac1"]

        if(hraci["Hrac1"].get_barva == barva):
            hrac_dle_barvy = hraci["Hrac1"]
        else:
            hrac_dle_barvy = hraci["Hrac2"]

        statistiky = hrac_dle_barvy.get_statistiky
        pocet_kamenu = statistiky["pocet_vyvedenych_kamenu"]

        if(barva == "bila"):
            domecek_bila_lbl = Label(platno, text=textwrap.fill(f"{pocet_kamenu}/15", 2))
            domecek_bila_lbl.config(font=("Arial", 20), fg="white", bg="#843c24")
            domecek_bila_lbl.place(x=650, y=159)
        else:
            domecek_cerna_lbl = Label(platno, text=textwrap.fill(f"{pocet_kamenu}/15", 2))
            domecek_cerna_lbl.config(font=("Arial", 20), fg="white", bg="#843c24")
            domecek_cerna_lbl.place(x=650, y=459)

    def vytvorit_labely_domecku(platno : Canvas):
        domecek_bila_lbl = Label(platno, text=textwrap.fill("0/15", 2))
        domecek_bila_lbl.config(font=("Arial", 20), fg="white", bg="#843c24")
        domecek_bila_lbl.place(x=650, y=159)

        domecek_cerna_lbl = Label(platno, text=textwrap.fill("0/15", 2))
        domecek_cerna_lbl.config(font=("Arial", 20), fg="white", bg="#843c24")
        domecek_cerna_lbl.place(x=650, y=459)

    def zobraz_vyherce(platno : Canvas):
        vyherce = "Hrac1" # musi se dodelat 
        vyherce_lbl = Label(platno, text=f"Vyhral: {vyherce}")
        vyherce_lbl.config(font=("Arial", 20), fg="white", bg="#843c24")
        vyherce_lbl.place(x=400, y=150)

    def zobraz_statistiky(platno : Canvas):

        #"pocet_vyvedenych_kamenu" : 0,
        #"pocet_vyhozenych_kamenu" : 0,
        #"pocet_vyhozenych_svych_kamenu" : 0,
        #"prumerna_zivotnost_kamene" : 0.0} 


        hraci = StavHry.get_hraci()
        hrac1 = hraci["Hrac1"]
        hrac2 = hraci["Hrac2"]

        hrac1_statistiky = hrac1.get_statistiky

        hrac1_pocet_vyvedenych_kamenu = hrac1_statistiky["pocet_vyvedenych_kamenu"]
        hrac1_pocet_vyhozenych_kamenu = hrac1_statistiky["pocet_vyhozenych_kamenu"]
        hrac1_pocet_vyhozenych_svych_kamenu = hrac1_statistiky["pocet_vyhozenych_svych_kamenu"]
        hrac1_prumerna_zivotnost_kamene = hrac1_statistiky["prumerna_zivotnost_kamene"]

        hrac1_statistiky_lbl = Label(platno, text=f"Statistiky Hrace1 ({hrac1.get_barva}):\nPocet vyvedenych kamenu: {hrac1_pocet_vyvedenych_kamenu}\nPocet vyhozenych kamenu nepratele: {hrac1_pocet_vyhozenych_kamenu}\nPocet kamenu na baru: {hrac1_pocet_vyhozenych_svych_kamenu}\nPrumerna zivotnost kamene: {hrac1_prumerna_zivotnost_kamene}")
        hrac1_statistiky_lbl.config(font=("Arial", 18), fg="white", bg="#843c24")
        hrac1_statistiky_lbl.place(x=20, y=250)


        hrac2_statistiky = hrac1.get_statistiky

        hrac2_pocet_vyvedenych_kamenu = hrac2_statistiky["pocet_vyvedenych_kamenu"]
        hrac2_pocet_vyhozenych_kamenu = hrac2_statistiky["pocet_vyhozenych_kamenu"]
        hrac2_pocet_vyhozenych_svych_kamenu = hrac2_statistiky["pocet_vyhozenych_svych_kamenu"]
        hrac2_prumerna_zivotnost_kamene = hrac2_statistiky["prumerna_zivotnost_kamene"]

        hrac2_statistiky_lbl = Label(platno, text=f"Statistiky Hrace2 ({hrac2.get_barva}):\nPocet vyvedenych kamenu: {hrac2_pocet_vyvedenych_kamenu}\nPocet vyhozenych kamenu nepratele: {hrac2_pocet_vyhozenych_kamenu}\nPocet kamenu na baru: {hrac2_pocet_vyhozenych_svych_kamenu}\nPrumerna zivotnost kamene: {hrac2_prumerna_zivotnost_kamene}")
        hrac2_statistiky_lbl.config(font=("Arial", 18), fg="white", bg="#843c24")
        hrac2_statistiky_lbl.place(x=510, y=250)