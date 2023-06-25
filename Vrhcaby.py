import tkinter as tk
import random
import json
from tkinter import *
from tkinter import messagebox, Message, font
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path


import SoundManager 
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

    with open("vrhcaby_json.json", "w") as soubor:
        soubor.write(json_objects)

def load_file():
    with open("vrhcaby_json.json", "r") as json_file:
        data = json.load(json_file)
        
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

    ulozit_hru = Image.open("save.png") 
    ulozit_hru_tk = ImageTk.PhotoImage(ulozit_hru)
    ulozit_hru_button = Button(platno_hra, image=ulozit_hru_tk,
                                 command=lambda: save_file())
    ulozit_hru_button.config(
        width=ulozit_hru_tk.width(), height=ulozit_hru_tk.height())
    platno_hra.create_window(830, 480, window=ulozit_hru_button)

    zpet_menu = Image.open("menu.png") 
    zpet_menu_tk = ImageTk.PhotoImage(zpet_menu)
    zpet_menu_button = Button(platno_hra, image=zpet_menu_tk,
                                 command=lambda: HerniDeska.zpet_do_menu())
    zpet_menu_button.config(
        width=zpet_menu_tk.width(), height=zpet_menu_tk.height())
    platno_hra.create_window(830, 600, window=zpet_menu_button)

    @classmethod
    def vytvor_pointy(cls):
        Zasobnik.zasobniky = []
        # 5 - maximalni pocet kamenu na danem pointu (z duvodu mista na mape vyuzivame tzv. Egyptian rule)
        for i in range(1, 24+2):
            Zasobnik.zasobniky.append(Zasobnik(5))
        return Zasobnik.zasobniky

    @classmethod
    def hrat_button_click(cls):
        HerniDeska.priprav_hraci_desku(cls)

        Hra.pridej_zakladni_kameny(cls)
        Hra.roztrid_kameny_do_zasobniku(cls)

        Hra.rozhodni_o_barve_hrace()
        StavHry.set_stav("hrac1_kostka")
        Label_manager.zmena_stavu(HerniDeska.platno_hra, "","Ceka se na hod dvojkostkou Hrace1")
        Label_manager.vytvorit_labely_domecku(HerniDeska.platno_hra)

    @classmethod
    def pokracovat_button_click(cls):
        HerniDeska.priprav_hraci_desku(cls)
        
        file_path = open_file()
        Hra.loadni_kameny(cls, file_path)

    def priprav_hraci_desku(cls):
        HerniDeska.shovej_menu()
        HerniDeska.vykresli_hraci_desku()
        Hra.pridej_pozice(cls)
        HerniDeska.vytvor_pointy()

    def zpet_do_menu():
        HerniDeska.platno_hra.pack_forget()
        HerniDeska.platno_menu.pack()        
        
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

    hrac1 = "" # vzdy konzolovy_hrac
    hrac2 = "" # dle radiobuttonu v menu

    def __init__(self, hra):
        self.hra = hra
        self.platno = HerniDeska()
        Herni_kamen.root = hra

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
        
        for kamen in mapa_kamenu.keys():
            slovnik = {
                str(kamen): {
                    "barva_kamene": kamen.barva_kamene,
                    "historie": kamen.historie,
                    "pozice_kamene": kamen.pozice_kamene
                }
            }
            pole_kamenu.append(slovnik)        
        return pole_kamenu 

    def hrac1_k_ulozeni():
        hraci = StavHry.get_hraci()
        hrac = hraci["Hrac1"]
        
        slovnik = {
            "Hrac1": {
                "barva": hrac.get_barva,
                "vysledky_dvojkostky": hrac.get_vysledky,
                "mozne_tahy": hrac.get_mozne_tahy,
                "prvni_hod": hrac.get_prvni_hod,
                "pocet_hozenych_cisel": hrac.get_hozeny_pocet,
                "odehrane_kameny": hrac.get_odehrane_kameny,
                "statistiky": hrac.get_statistiky

            }
        }
      
        return slovnik 

    def hrac2_k_ulozeni():
        hraci = StavHry.get_hraci()
        hrac = hraci["Hrac2"]
        
        slovnik = {
            "Hrac2": {
                "barva": hrac.get_barva,
                "vysledky_dvojkostky": hrac.get_vysledky,
                "mozne_tahy": hrac.get_mozne_tahy,
                "prvni_hod": hrac.get_prvni_hod,
                "pocet_hozenych_cisel": hrac.get_hozeny_pocet,
                "odehrane_kameny": hrac.get_odehrane_kameny,
                "statistiky": hrac.get_statistiky

            }
        }

        if(HerniDeska.get_zvoleny_souper() == "AI"):
            slovnik["Hrac2"]["aktualni_pointy"] = hrac.get_aktualni_pointy
      
        return slovnik 
    
    def loadni_kameny(self, json_file):
        mapa = Mapa_pozic._mapa_pozic
        mapa_kamenu = Mapa_kamenu._mapa_kamenu

        data = json.load(open(json_file))
        for i in data:
            list_of_values = list(i.values())
            mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, list_of_values[0]["barva_kamene"], tuple(list_of_values[0]["pozice_kamene"]), list_of_values[0]["historie"])] = mapa[tuple(list_of_values[0]["pozice_kamene"])]

    def loadni_hrace(self, json_file):
        
        ...

    def pridej_zakladni_kameny(self):
        mapa = Mapa_pozic._mapa_pozic
        mapa_kamenu = Mapa_kamenu._mapa_kamenu

        puvodni_cerny_kameny = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0]
        puvodni_bily_kameny = [0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]

        # Cerne zakladni pozice
        for i in range(len(puvodni_cerny_kameny)):
            for j in range(puvodni_cerny_kameny[i]):
                mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "bila", (i+1, j+1), [(i+1, j+1)])] = mapa[(i+1, j+1)]

        # Bile zakladni pozice
        for i in range(len(puvodni_bily_kameny)):
            for j in range(puvodni_bily_kameny[i]):
                mapa_kamenu[Herni_kamen(HerniDeska.platno_hra, "cerna", (i+1, j+1), [(i+1, j+1)])] = mapa[(i+1, j+1)]

    def roztrid_kameny_do_zasobniku(self):
    # roztridi kameny do zasobniku (zasobnik[1 az 24 - odpovida pointum na mape])
        mapa_kamenu = Mapa_kamenu._mapa_kamenu
        for kamen in mapa_kamenu.keys(): 
            Zasobnik.zasobniky[kamen.pozice_kamene[0]].push(kamen)

    def pridej_pozice(self):  # naplni vsechny pointy maximalnim poctem kamenu (5ti) - tyto kameny jsou skryte a pouzivane pro posuny a pro napovedu dalsich tahu
        mapa = Mapa_pozic._mapa_pozic

        # i -> 1-6 | j -> 1-5
        # dolni pulka
        x = 610
        for i in range(1, 12+1):
            y = 609
            for j in range(1, 5+1):                               
                mapa[(i, j)] = Pozice(HerniDeska.platno_hra, True, [x, y])
                y -= 50
            if i % 6 != 0:    
                x -= 47
            else:
                x -= 80

        # horni pulka
        x = 59
        for i in range(13, 24+1):
            y = 59
            for j in range(1, 5+1):                               
                mapa[(i, j)] = Pozice(HerniDeska.platno_hra, True, [x, y])
                y += 50
            if i % 6 != 0:    
                x += 47
            else:
                x += 80
        
        # Bar
        mapa[(99,2)] = Pozice(HerniDeska.platno_hra, True, [335,259]) # Bily
        mapa[(99,1)] = Pozice(HerniDeska.platno_hra, True, [335,409]) # Cerny   
        
        # Domecky
        mapa[(0,2)] = Pozice(HerniDeska.platno_hra, True, [665,109]) # Cerny   
        mapa[(0,1)] = Pozice(HerniDeska.platno_hra, True, [665,559]) # Bily

    def hod_kostkou():
        hraci = StavHry.get_hraci()
        hrac1 = hraci["Hrac1"]
        hrac2 = hraci["Hrac2"]


        if(StavHry.get_stav() == "hrac1_kostka" or StavHry.get_stav() == "hrac2_kostka"):
            Dvojkostka.zvoleny_souper = HerniDeska.get_zvoleny_souper()
            Dvojkostka.rozehrat(HerniDeska.platno_hra)
            SoundManager.throw_sound.play() # Pustí throw.mp3 sound z soundManageru
        else:
            if(StavHry.get_stav() == "Hrac1" or StavHry.get_stav() == "Hrac2"):
                if(len(hraci[StavHry.get_stav()].get_vysledky) <= 0):
                    hraci[StavHry.get_stav()].set_vysledky(Dvojkostka.hod_dvojkostkou())
                    if(len(hraci[StavHry.get_stav()].get_vysledky) == 4):
                        hraci[StavHry.get_stav()].set_hozeny_pocet(4)
                    else:
                        hraci[StavHry.get_stav()].set_hozeny_pocet(2)
                    SoundManager.throw_sound.play()
                    Label_manager.zobraz_vysledky_dvojkostky(HerniDeska.platno_hra, hraci[StavHry.get_stav()].get_barva, hraci[StavHry.get_stav()].get_vysledky)
                    if(Herni_kamen.kontrola_hrac_muze_hrat(HerniDeska.platno_hra, hraci[StavHry.get_stav()].get_barva, hraci[StavHry.get_stav()].get_vysledky) == False):
                        hraci["Hrac1"].get_odehrane_kameny.clear()
                        hraci["Hrac2"].get_odehrane_kameny.clear()
                        hraci[StavHry.get_stav()].get_vysledky.clear()
                        if(StavHry.get_stav() == "Hrac1"):
                            StavHry.set_stav("Hrac2")
                            Label_manager.zmena_stavu(HerniDeska.platno_hra, "tojejedno", "Hrac1 nemohl hrat, hraje Hrac2.")
                        else:
                            StavHry.set_stav("Hrac1")  
                            Label_manager.zmena_stavu(HerniDeska.platno_hra, "tojejedno", "Hrac2 nemohl hrat, hraje Hrac1.")

                else:
                    messagebox.showinfo("Informace", f"Jiz jste si kostkou hodili. Nyni, pokud mozno, hrajte s kameny. Vase barva: {hraci[StavHry.get_stav()].get_barva}")

        if(StavHry.get_stav() == "hrac2_kostka"):
            Label_manager.zmena_stavu(HerniDeska.platno_hra, "","Ceka se na hod dvojkostkou Hrace2")

        if(StavHry.get_stav() == "Hrac1"):
            Label_manager.zmena_stavu(HerniDeska.platno_hra, "",f"Hrac1 hraje ({hrac1.get_barva}). Hodte si dvojkostkou!")

        if(StavHry.get_stav() == "Hrac2"):
            if(HerniDeska.get_zvoleny_souper() == "AI"):
                Label_manager.zmena_stavu(HerniDeska.platno_hra, "",f"Hrac2 hraje ({hrac2.get_barva} - AI)")
                if(len(hrac2.get_vysledky) <= 0):
                    Hra.hod_kostkou()
                else:
                    Herni_kamen.AI_tah(Herni_kamen.root, HerniDeska.platno_hra)
            else:
                Label_manager.zmena_stavu(HerniDeska.platno_hra, "",f"Hrac2 hraje ({hrac2.get_barva}). Hodte si dvojkostkou!")

        # Pouze na otestovani ulozeni hry
        #save_file()

if __name__ == "__main__":
    app = Hra(root)
    root.mainloop()


    # PRACE DAL:
    # Zda se mi, ze si nejak vymysli tahy nebo ze hraje s vice kameny, nez by mela
    # Zpomalit ji, aby to vypadalo realneji