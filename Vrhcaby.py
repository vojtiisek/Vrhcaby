import tkinter as tk
import random
import json
from tkinter import *
from tkinter import messagebox, Message, font
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path

from Dvojkostka import Dvojkostka
from Herni_kamen import Herni_kamen
from Pozice import Pozice
from Mapa_pozic import Mapa_pozic
from Mapa_kamenu import Mapa_kamenu
from Zasobnik import Zasobnik
from Konzolovy_hrac import Konzolovy_Hrac
from AI_hrac import AI_Hrac
from StavHry import StavHry
from Label_manager import Label_manager

root = tk.Tk()

def open_file():
    return filedialog.askopenfilename(title="Vyberte soubor", filetypes=([("JSON files", "*.json")]))

def save_file():
    json_objects = json.dumps(Hra.pole_kamenu_k_ulozeni(), indent=4)

    with open("vrhcaby_json", "w") as soubor:
        soubor.write(json_objects)
    print("Hra ulozena")
        
class HerniDeska:
    # Okno
    hra = root
    hra.resizable(False, False)
    hra.geometry("964x669")
    hra.title("Vrhcaby")

    # Pozadi menu
    pozadi_obrazek = Image.open("wooden_table_background.jpg")
    pozadi_menu = ImageTk.PhotoImage(pozadi_obrazek)

    # Platno - menu
    platno_menu = tk.Canvas(hra, width=964, height=669)
    platno_menu.create_image(0, 0, image=pozadi_menu, anchor=tk.NW)
    platno_menu.pack()

    # Ikona
    icon = Image.open("vrhcaby_icon.png")
    icon_tk = ImageTk.PhotoImage(icon)
    hra.wm_iconphoto(True, icon_tk)

    # Tlacitka
    # Tlacitko "Hrat"
    start_game_bg = Image.open("start_button.png")
    start_game_bg_tk = ImageTk.PhotoImage(start_game_bg)
    start_game_button = Button(platno_menu, image=start_game_bg_tk,
                               command=lambda: HerniDeska.hrat_button_click(), bd=0, highlightthickness=0)
    start_game_button.config(
        width=start_game_bg_tk.width(), height=start_game_bg_tk.height())
    platno_menu.create_window(480, 300, window=start_game_button)

    # Tlacitko "Pokracovat"
    continue_game_bg = Image.open("continue_button.png")
    continue_game_bg_tk = ImageTk.PhotoImage(continue_game_bg)
    continue_game_bg_button = Button(platno_menu, image=continue_game_bg_tk, 
                                     command=lambda: HerniDeska.pokracovat_button_click(), bd=0, highlightthickness=0)
    continue_game_bg_button.config(
        width=continue_game_bg_tk.width(), height=continue_game_bg_tk.height())
    platno_menu.create_window(480, 430, window=continue_game_bg_button)

    # Tlacitko "Ukoncit hru"
    quit_game_bg = Image.open("quit_game_button.png") 
    quit_game_bg_tk = ImageTk.PhotoImage(quit_game_bg)
    quit_game_bg_button = Button(platno_menu, image=quit_game_bg_tk,
                                 command=lambda: HerniDeska.ukoncit_hru(), bd=0, highlightthickness=0)
    quit_game_bg_button.config(
        width=quit_game_bg_tk.width(), height=quit_game_bg_tk.height())
    platno_menu.create_window(480, 560, window=quit_game_bg_button)

    # Radiobuttony pro zvoleni oponenta
    radio_var = tk.StringVar()
    radio_var.set("AI")
    font_radiobuttons = font.Font(family="Arial", size=14)

    radio_button1 = tk.Radiobutton(hra, text="Hra proti AI", variable=radio_var, value="AI", font=font_radiobuttons, bg="#cb8742")
    radio_button2 = tk.Radiobutton(hra, text="Hra proti cloveku", variable=radio_var, value="KonzolovyHrac", font=font_radiobuttons, bg="#cb8742")

    platno_menu.create_window(820, 270, window=radio_button1)
    platno_menu.create_window(840, 330, window=radio_button2)

    # Pozadi - hra
    pozadi_obrazek_hra = Image.open("vrhcaby_mapa.jpg")
    pozadi_hra = ImageTk.PhotoImage(pozadi_obrazek_hra)
    # Platno - hra
    platno_hra = tk.Canvas(hra, width=964, height=669)
    platno_hra.create_image(0, 0, image=pozadi_hra, anchor=tk.NW)
    platno_hra.pack_forget()

    kostky_textura = Image.open("dice.jpg") 
    kostky_textura_tk = ImageTk.PhotoImage(kostky_textura)
    kostky_button = Button(platno_hra, image=kostky_textura_tk,
                                 command=lambda: Hra.hod_kostkou())
    kostky_button.config(
        width=kostky_textura_tk.width(), height=kostky_textura_tk.height())
    platno_hra.create_window(830, 360, window=kostky_button)

    @classmethod
    def vytvor_pointy(cls):
        Zasobnik.zasobniky = []
        # 5 - maximalni pocet kamenu na danem pointu (z duvodu mista na mape vyuzivame tzv. Egyptian rule)
        for i in range(1, 24+2):
            Zasobnik.zasobniky.append(Zasobnik(5))
        return Zasobnik.zasobniky

    @classmethod
    def hrat_button_click(cls):
        HerniDeska.shovej_menu()
        HerniDeska.vykresli_hraci_desku()
        Hra.pridej_pozice(cls)
        HerniDeska.vytvor_pointy()
        Hra.pridej_zakladni_kameny(cls)
        Hra.rozhodni_o_barve_hrace()
        StavHry.set_stav("hrac1_kostka")
        print(StavHry.get_stav())
        Label_manager.zmena_stavu(HerniDeska.platno_hra, "","Ceka se na hod dvojkostkou Hrace1")

    @classmethod
    def pokracovat_button_click(cls):
        HerniDeska.shovej_menu()
        HerniDeska.vykresli_hraci_desku()
        Hra.pridej_pozice(cls)
        HerniDeska.vytvor_pointy()
        file_path = open_file()
        Hra.loadni_kameny(file_path)
        

    def vysledek_hodu_kostkami(cls, hrac_barva : str, vysledek : list):
        #hrac_barva = Hra.get_aktualni_hrac()._barva_hrace

        ...


    @classmethod
    def ukoncit_hru(cls):
        HerniDeska.hra.destroy()

    @classmethod
    def start(cls):
        pass

    @classmethod
    def vykresli_hraci_desku(cls):
        HerniDeska.platno_hra.pack()

    @classmethod
    def shovej_menu(cls):
        HerniDeska.platno_menu.pack_forget()

    def get_zvoleny_souper() -> str:
        return HerniDeska.radio_var.get()

class Hra:

    hrac1 = "" #vzdy konzolovy_hrac
    hrac2 = "" # dle radiobuttonu v menu

    def __init__(self, hra):
        self.hra = hra
        self.platno = HerniDeska()

    def rozhodni_o_barve_hrace():
        barva_hrace = "error"
        volba = random.randint(1,6)

        if(volba == 1 or volba == 3 or volba == 5):
            barva_hrace = "bila"
        elif(volba == 2 or volba == 4 or volba == 6):
            barva_hrace = "cerna"
        else:
            messagebox.showinfo("Chyba", "Vyskytla se chyba pri vyberu barvy hrace.")
        Herni_kamen.barva_hrace = barva_hrace
        if(barva_hrace == "bila"):
            Hra.hrac1 = Konzolovy_Hrac(barva_hrace)
            if HerniDeska.get_zvoleny_souper() == "AI" :
                Hra.hrac2 = AI_Hrac("cerna")
                messagebox.showinfo("Informace", "Vase barva je: BILA")
            else:
                Hra.hrac2 = Konzolovy_Hrac("cerna")
        else:
            Hra.hrac1 = Konzolovy_Hrac(barva_hrace)
            if HerniDeska.get_zvoleny_souper() == "AI" :
                Hra.hrac2 = AI_Hrac("bila")
                messagebox.showinfo("Informace", "Vase barva je: CERNA")
            else:
                Hra.hrac2 = Konzolovy_Hrac("bila")

        StavHry.add_hrac("Hrac1", Hra.hrac1)
        StavHry.add_hrac("Hrac2", Hra.hrac2)


    def pole_kamenu_k_ulozeni():
        mapa_kamenu = Mapa_kamenu._mapa_kamenu
        pole_kamenu = []
        # mapa_kamenu.keys()
        for kamen in mapa_kamenu:
            slovnik = {
                "barva_kamene": kamen.barva_kamene,
                "historie": kamen.historie,
                "pozice_kamene": kamen.pozice_kamene
            }
            pole_kamenu.append(slovnik)        
        return pole_kamenu 
    
    def loadni_kameny(self, json_file):
        pass

    def pridej_zakladni_kameny(self):
        mapa = Mapa_pozic._mapa_pozic
        mapa_kamenu = Mapa_kamenu._mapa_kamenu

        # Cerne zakladni pozice
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (1,1))] = mapa[(1,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (1,2))] = mapa[(1,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (12,1))] = mapa[(12,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (12,2))] = mapa[(12,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (12,3))] = mapa[(12,3)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (12,4))] = mapa[(12,4)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (12,5))] = mapa[(12,5)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (17,1))] = mapa[(17,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (17,2))] = mapa[(17,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (17,3))] = mapa[(17,3)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (19,1))] = mapa[(19,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (19,2))] = mapa[(19,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (19,3))] = mapa[(19,3)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (19,4))] = mapa[(19,4)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (19,5))] = mapa[(19,5)]

        # Bile zakladni pozice

        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (24,1))] = mapa[(24,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (24,2))] = mapa[(24,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (13,1))] = mapa[(13,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (13,2))] = mapa[(13,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (13,3))] = mapa[(13,3)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (13,4))] = mapa[(13,4)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (13,5))] = mapa[(13,5)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (8,1))] = mapa[(8,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (8,2))] = mapa[(8,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (8,3))] = mapa[(8,3)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (6,1))] = mapa[(6,1)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (6,2))] = mapa[(6,2)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (6,3))] = mapa[(6,3)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (6,4))] = mapa[(6,4)]
        mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (6,5))] = mapa[(6,5)]

        for kamen in Mapa_kamenu._mapa_kamenu.keys(): # roztridi kameny do zasobniku (zasobnik[1 az 24 - odpovida pointum na mape])
            Zasobnik.zasobniky[kamen.pozice_kamene[0]].push(kamen)
            kamen.pridej_pozici_do_historie()

        #print([i.barva_kamene for i in mapa_kamenu])
        #print([i.pozice_kamene for i in mapa_kamenu])

    def pridej_pozice(self):  # naplni vsechny pointy maximalnim poctem kamenu (5ti) - tyto kameny jsou skryte a pouzivane pro posuny a pro napovedu dalsich tahu
        mapa = Mapa_pozic._mapa_pozic

        mapa[(1,1)] = Pozice(HerniDeska.platno_hra, True, [610,609]) 
        mapa[(1,2)] = Pozice(HerniDeska.platno_hra, True, [610,559])
        mapa[(1,3)] = Pozice(HerniDeska.platno_hra, True, [610,509])
        mapa[(1,4)] = Pozice(HerniDeska.platno_hra, True, [610,459])
        mapa[(1,5)] = Pozice(HerniDeska.platno_hra, True, [610,409])

        mapa[(2,1)] = Pozice(HerniDeska.platno_hra, True, [562,609])
        mapa[(2,2)] = Pozice(HerniDeska.platno_hra, True, [562,559])
        mapa[(2,3)] = Pozice(HerniDeska.platno_hra, True, [562,509])
        mapa[(2,4)] = Pozice(HerniDeska.platno_hra, True, [562,459])
        mapa[(2,5)] = Pozice(HerniDeska.platno_hra, True, [562,409])


        mapa[(3,1)] = Pozice(HerniDeska.platno_hra, True, [515,609])
        mapa[(3,2)] = Pozice(HerniDeska.platno_hra, True, [515,559])
        mapa[(3,3)] = Pozice(HerniDeska.platno_hra, True, [515,509])
        mapa[(3,4)] = Pozice(HerniDeska.platno_hra, True, [515,459])
        mapa[(3,5)] = Pozice(HerniDeska.platno_hra, True, [515,409])

        mapa[(4,1)] = Pozice(HerniDeska.platno_hra, True, [468,609])
        mapa[(4,2)] = Pozice(HerniDeska.platno_hra, True, [468,559])
        mapa[(4,3)] = Pozice(HerniDeska.platno_hra, True, [468,509])
        mapa[(4,4)] = Pozice(HerniDeska.platno_hra, True, [468,459])
        mapa[(4,5)] = Pozice(HerniDeska.platno_hra, True, [468,409])

        mapa[(5,1)] = Pozice(HerniDeska.platno_hra, True, [421,609])
        mapa[(5,2)] = Pozice(HerniDeska.platno_hra, True, [421,559])
        mapa[(5,3)] = Pozice(HerniDeska.platno_hra, True, [421,509])
        mapa[(5,4)] = Pozice(HerniDeska.platno_hra, True, [421,459])
        mapa[(5,5)] = Pozice(HerniDeska.platno_hra, True, [421,409])


        mapa[(6,1)] = Pozice(HerniDeska.platno_hra, True, [374,609])
        mapa[(6,2)] = Pozice(HerniDeska.platno_hra, True, [374,559])
        mapa[(6,3)] = Pozice(HerniDeska.platno_hra, True, [374,509])
        mapa[(6,4)] = Pozice(HerniDeska.platno_hra, True, [374,459])
        mapa[(6,5)] = Pozice(HerniDeska.platno_hra, True, [374,409])


        mapa[(7,1)] = Pozice(HerniDeska.platno_hra, True, [294,609])
        mapa[(7,2)] = Pozice(HerniDeska.platno_hra, True, [294,559])
        mapa[(7,3)] = Pozice(HerniDeska.platno_hra, True, [294,509])
        mapa[(7,4)] = Pozice(HerniDeska.platno_hra, True, [294,459])
        mapa[(7,5)] = Pozice(HerniDeska.platno_hra, True, [294,409])

        mapa[(8,1)] = Pozice(HerniDeska.platno_hra, True, [247,609])
        mapa[(8,2)] = Pozice(HerniDeska.platno_hra, True, [247,559])
        mapa[(8,3)] = Pozice(HerniDeska.platno_hra, True, [247,509])
        mapa[(8,4)] = Pozice(HerniDeska.platno_hra, True, [247,459])
        mapa[(8,5)] = Pozice(HerniDeska.platno_hra, True, [247,409])

        mapa[(9,1)] = Pozice(HerniDeska.platno_hra, True, [200,609])
        mapa[(9,2)] = Pozice(HerniDeska.platno_hra, True, [200,559])
        mapa[(9,3)] = Pozice(HerniDeska.platno_hra, True, [200,509])
        mapa[(9,4)] = Pozice(HerniDeska.platno_hra, True, [200,459])
        mapa[(9,5)] = Pozice(HerniDeska.platno_hra, True, [200,409])

        mapa[(10,1)] = Pozice(HerniDeska.platno_hra, True, [153,609])
        mapa[(10,2)] = Pozice(HerniDeska.platno_hra, True, [153,559])
        mapa[(10,3)] = Pozice(HerniDeska.platno_hra, True, [153,509])
        mapa[(10,4)] = Pozice(HerniDeska.platno_hra, True, [153,459])
        mapa[(10,5)] = Pozice(HerniDeska.platno_hra, True, [153,409])

        mapa[(11,1)]= Pozice(HerniDeska.platno_hra, True, [106,609])
        mapa[(11,2)] = Pozice(HerniDeska.platno_hra, True, [106,559])
        mapa[(11,3)] = Pozice(HerniDeska.platno_hra, True, [106,509])
        mapa[(11,4)] = Pozice(HerniDeska.platno_hra, True, [106,459])
        mapa[(11,5)] = Pozice(HerniDeska.platno_hra, True, [106,409])

        mapa[(12,1)] = Pozice(HerniDeska.platno_hra, True, [59,609])
        mapa[(12,2)] = Pozice(HerniDeska.platno_hra, True, [59,559])
        mapa[(12,3)] = Pozice(HerniDeska.platno_hra, True, [59,509])
        mapa[(12,4)] = Pozice(HerniDeska.platno_hra, True, [59,459])
        mapa[(12,5)] = Pozice(HerniDeska.platno_hra, True, [59,409])


        # horni pulka

        mapa[(24,1)] = Pozice(HerniDeska.platno_hra, True, [610,59])
        mapa[(24,2)] = Pozice(HerniDeska.platno_hra, True, [610,109])
        mapa[(24,3)] = Pozice(HerniDeska.platno_hra, True, [610,159])
        mapa[(24,4)] = Pozice(HerniDeska.platno_hra, True, [610,209])
        mapa[(24,5)] = Pozice(HerniDeska.platno_hra, True, [610,259])

        mapa[(23,1)] = Pozice(HerniDeska.platno_hra, True, [562,59])
        mapa[(23,2)] = Pozice(HerniDeska.platno_hra, True, [562,109])
        mapa[(23,3)] = Pozice(HerniDeska.platno_hra, True, [562,159])
        mapa[(23,4)] = Pozice(HerniDeska.platno_hra, True, [562,209])
        mapa[(23,5)] = Pozice(HerniDeska.platno_hra, True, [562,259])


        mapa[(22,1)] = Pozice(HerniDeska.platno_hra, True, [515,59])
        mapa[(22,2)] = Pozice(HerniDeska.platno_hra, True, [515,109])
        mapa[(22,3)] = Pozice(HerniDeska.platno_hra, True, [515,159])
        mapa[(22,4)] = Pozice(HerniDeska.platno_hra, True, [515,209])
        mapa[(22,5)] = Pozice(HerniDeska.platno_hra, True, [515,259])

        mapa[(21,1)] = Pozice(HerniDeska.platno_hra, True, [468,59])
        mapa[(21,2)] = Pozice(HerniDeska.platno_hra, True, [468,109])
        mapa[(21,3)] = Pozice(HerniDeska.platno_hra, True, [468,159])
        mapa[(21,4)] = Pozice(HerniDeska.platno_hra, True, [468,209])
        mapa[(21,5)] = Pozice(HerniDeska.platno_hra, True, [468,259])

        mapa[(20,1)] = Pozice(HerniDeska.platno_hra, True, [421,59])
        mapa[(20,2)] = Pozice(HerniDeska.platno_hra, True, [421,109])
        mapa[(20,3)] = Pozice(HerniDeska.platno_hra, True, [421,159])
        mapa[(20,4)] = Pozice(HerniDeska.platno_hra, True, [421,209])
        mapa[(20,5)] = Pozice(HerniDeska.platno_hra, True, [421,259])


        mapa[(19,1)] = Pozice(HerniDeska.platno_hra, True, [374,59])
        mapa[(19,2)] = Pozice(HerniDeska.platno_hra, True, [374,109])
        mapa[(19,3)] = Pozice(HerniDeska.platno_hra, True, [374,159])
        mapa[(19,4)] = Pozice(HerniDeska.platno_hra, True, [374,209])
        mapa[(19,5)] = Pozice(HerniDeska.platno_hra, True, [374,259])


        mapa[(18,1)] = Pozice(HerniDeska.platno_hra, True, [294,59])
        mapa[(18,2)] = Pozice(HerniDeska.platno_hra, True, [294,109])
        mapa[(18,3)] = Pozice(HerniDeska.platno_hra, True, [294,159])
        mapa[(18,4)] = Pozice(HerniDeska.platno_hra, True, [294,209])
        mapa[(18,5)] = Pozice(HerniDeska.platno_hra, True, [294,259])

        mapa[(17,1)] = Pozice(HerniDeska.platno_hra, True, [247,59])
        mapa[(17,2)] = Pozice(HerniDeska.platno_hra, True, [247,109])
        mapa[(17,3)] = Pozice(HerniDeska.platno_hra, True, [247,159])
        mapa[(17,4)] = Pozice(HerniDeska.platno_hra, True, [247,209])
        mapa[(17,5)] = Pozice(HerniDeska.platno_hra, True, [247,259])

        mapa[(16,1)] = Pozice(HerniDeska.platno_hra, True, [200,59])
        mapa[(16,2)] = Pozice(HerniDeska.platno_hra, True, [200,109])
        mapa[(16,3)] = Pozice(HerniDeska.platno_hra, True, [200,159])
        mapa[(16,4)] = Pozice(HerniDeska.platno_hra, True, [200,209])
        mapa[(16,5)] = Pozice(HerniDeska.platno_hra, True, [200,259])

        mapa[(15,1)] = Pozice(HerniDeska.platno_hra, True, [153,59])
        mapa[(15,2)] = Pozice(HerniDeska.platno_hra, True, [153,109])
        mapa[(15,3)] = Pozice(HerniDeska.platno_hra, True, [153,159])
        mapa[(15,4)] = Pozice(HerniDeska.platno_hra, True, [153,209])
        mapa[(15,5)] = Pozice(HerniDeska.platno_hra, True, [153,259])

        mapa[(14,1)] = Pozice(HerniDeska.platno_hra, True, [106,59])
        mapa[(14,2)] = Pozice(HerniDeska.platno_hra, True, [106,109])
        mapa[(14,3)] = Pozice(HerniDeska.platno_hra, True, [106,159])
        mapa[(14,4)] = Pozice(HerniDeska.platno_hra, True, [106,209])
        mapa[(14,5)] = Pozice(HerniDeska.platno_hra, True, [106,259])

        mapa[(13,1)] = Pozice(HerniDeska.platno_hra, True, [59,59])
        mapa[(13,2)] = Pozice(HerniDeska.platno_hra, True, [59,109])
        mapa[(13,3)] = Pozice(HerniDeska.platno_hra, True, [59,159])
        mapa[(13,4)] = Pozice(HerniDeska.platno_hra, True, [59,209])
        mapa[(13,5)] = Pozice(HerniDeska.platno_hra, True, [59,259])

        # Bar

        mapa[(99,1)] = Pozice(HerniDeska.platno_hra, True, [335,259]) # Bily
        mapa[(99,2)] = Pozice(HerniDeska.platno_hra, True, [335,409]) # Cerny        

    def hod_kostkou():
        hraci = StavHry.get_hraci()
        hrac1 = hraci["Hrac1"]
        hrac2 = hraci["Hrac2"]

        if(StavHry.get_stav() == "hrac1_kostka" or StavHry.get_stav() == "hrac2_kostka"):
            print("rozehrani")
            Dvojkostka.rozehrat()
        else:
            if(StavHry.get_stav() == "Hrac1" or StavHry.get_stav() == "Hrac2"):
                if(len(hraci[StavHry.get_stav()].get_vysledky) <= 0):
                    hraci[StavHry.get_stav()].set_vysledky(Dvojkostka.hod_dvojkostkou())
                else:
                    messagebox.showinfo("Informace", f"Jiz jste si kostkou hodili. Nyni, pokud mozno, hrajte s kameny. Vase barva: {hraci[StavHry.get_stav()].get_barva}")

        if(StavHry.get_stav() == "hrac2_kostka"):
            Label_manager.zmena_stavu(HerniDeska.platno_hra, "","Ceka se na hod dvojkostkou Hrace2")

        if(StavHry.get_stav() == "Hrac1"):
            Label_manager.zmena_stavu(HerniDeska.platno_hra, "",f"Hrac1 hraje ({hrac1.get_barva}). Hodte si dvojkostkou!")

        if(StavHry.get_stav() == "Hrac2"):
            Label_manager.zmena_stavu(HerniDeska.platno_hra, "",f"Hrac2 hraje ({hrac2.get_barva}). Hodte si dvojkostkou!")


        # Pouze na otestovani ulozeni hry
        save_file()

if __name__ == "__main__":
    app = Hra(root)
    root.mainloop()



    # DALE: Dokoncit tahy - ruzne kameny na 2 nebo az 4 tahy (vypocet vzdalenosti pointu A->B, odebrani tohoto hodu, neboli vysledku dvojkostky, z vysledku hrace.)
    #       Stridani stavu hry mezi Hrac1 a Hrac2 - dle pravidel, pravdepodobne bude reseno pri presunech kamenu