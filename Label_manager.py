from tkinter import Tk as tk
from tkinter import Label, Canvas
import textwrap

class Label_manager:

    def zmena_pozice(platno : Canvas, barva : str, z_pozice : tuple, na_pozici: tuple, sebrany_kamen : tuple) -> None:
        if(z_pozice == (99,99)):
            z_pozice_processed = "Bar"
        else:
            z_pozice_processed = z_pozice
        if(na_pozici == (99,99)):
            na_pozici_processed = "Bar"
        else:
            na_pozici_processed = na_pozici

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