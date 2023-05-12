from this import d
import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image
from pathlib import Path

from Herni_kamen import Herni_kamen
from Pozice import Pozice

root = tk.Tk()

class HerniDeska:

    def __init__(cls):
        ...

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
    hra.wm_iconphoto(False, icon_tk)

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
    continue_game_bg_button = Button(
        platno_menu, image=continue_game_bg_tk, bd=0, highlightthickness=0)
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

    # Pozadi - hra
    pozadi_obrazek_hra = Image.open("vrhcaby_mapa.jpg")
    pozadi_hra = ImageTk.PhotoImage(pozadi_obrazek_hra)

    # Platno - hra
    platno_hra = tk.Canvas(hra, width=964, height=669)
    platno_hra.create_image(0, 0, image=pozadi_hra, anchor=tk.NW)
    platno_hra.pack_forget()

    mapa_pozic = {} # (point, vyska) : Pozice() ; napø. [1,1] : pozice1_1

    @classmethod
    def vytvor_pointy(cls):
        # 5 - maximalni pocet kamenu na danem pointu (z duvodu mista na mape vyuzivame tzv. Egyptian rule)
        zasobniky = []
        for i in range(1, 24+1):
            zasobniky.append(Zasobnik(5))
        print(zasobniky[0])
        print(zasobniky[1])
        return zasobniky

    @classmethod
    def pridej_kameny(cls):
        pass

    @classmethod
    def hrat_button_click(cls):
        HerniDeska.shovej_menu()
        HerniDeska.vykresli_hraci_desku()
        Hra.pridej_pozice(cls)

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

    #@classmethod
    #def platno_hra(cls):
    #    return HerniDeska.platno_hra


   #vytvor_pointy()
    #pridej_pozice()
    #pridej_kameny(None)

class Zasobnik:
    def __init__(self, max_size: int):
        self.zasobnik = []
        self.max_size = max_size

    def push(self, item) -> None:
        if (self.size >= self.max_size):
            pass
        else:
            self.zasobnik.append(item)

    def pop(self) -> None:
        if (len(self.zasobnik) > 0):
            self.zasobnik.pop(-1)
        else:
            pass

    def front(self):
        if (len(self.zasobnik) > 0):
            return self.zasobnik[0]
        else:
            pass

    def rear(self):
        if (len(self.zasobnik) > 0):
            return self.zasobnik[len(self.zasobnik)-1]
        else:
            pass

    def is_empty(self) -> bool:
        if (len(self.zasobnik) <= 0):
            return True
        else:
            return False

    def size(self) -> int:
        return len(self.zasobnik)


class Hra:
    def __init__(self, hra):
        self.hra = hra
        self.platno = HerniDeska()

    def pridej_pozice(self):  # naplni vsechny pointy maximalnim poctem kamenu (5ti) - tyto kameny jsou skryte a pouzivane pro posuny a pro napovedu dalsich tahu
        HerniDeska.mapa_pozic[(1,1)] = Pozice(HerniDeska.platno_hra, False, [610,609])
        HerniDeska.mapa_pozic[(1,2)] = Pozice(HerniDeska.platno_hra, False, [610,559])
        HerniDeska.mapa_pozic[(1,3)] = Pozice(HerniDeska.platno_hra, False, [610,509])
        HerniDeska.mapa_pozic[(1,4)] = Pozice(HerniDeska.platno_hra, False, [610,459])
        HerniDeska.mapa_pozic[(1,5)] = Pozice(HerniDeska.platno_hra, False, [610,409])

        HerniDeska.mapa_pozic[(2,1)] = Pozice(HerniDeska.platno_hra, False, [562,609])
        HerniDeska.mapa_pozic[(2,2)] = Pozice(HerniDeska.platno_hra, False, [562,559])
        HerniDeska.mapa_pozic[(2,3)] = Pozice(HerniDeska.platno_hra, False, [562,509])
        HerniDeska.mapa_pozic[(2,4)] = Pozice(HerniDeska.platno_hra, False, [562,459])
        HerniDeska.mapa_pozic[(2,5)] = Pozice(HerniDeska.platno_hra, False, [562,409])


        HerniDeska.mapa_pozic[(3,1)] = Pozice(HerniDeska.platno_hra, False, [515,609])
        HerniDeska.mapa_pozic[(3,2)] = Pozice(HerniDeska.platno_hra, False, [515,559])
        HerniDeska.mapa_pozic[(3,3)] = Pozice(HerniDeska.platno_hra, False, [515,509])
        HerniDeska.mapa_pozic[(3,4)] = Pozice(HerniDeska.platno_hra, False, [515,459])
        HerniDeska.mapa_pozic[(3,5)] = Pozice(HerniDeska.platno_hra, False, [515,409])

        HerniDeska.mapa_pozic[(4,1)] = Pozice(HerniDeska.platno_hra, False, [468,609])
        HerniDeska.mapa_pozic[(4,2)] = Pozice(HerniDeska.platno_hra, False, [468,559])
        HerniDeska.mapa_pozic[(4,3)] = Pozice(HerniDeska.platno_hra, False, [468,509])
        HerniDeska.mapa_pozic[(4,4)] = Pozice(HerniDeska.platno_hra, False, [468,459])
        HerniDeska.mapa_pozic[(4,5)] = Pozice(HerniDeska.platno_hra, False, [468,409])

        HerniDeska.mapa_pozic[(5,1)] = Pozice(HerniDeska.platno_hra, False, [421,609])
        HerniDeska.mapa_pozic[(5,2)] = Pozice(HerniDeska.platno_hra, False, [421,559])
        HerniDeska.mapa_pozic[(5,3)] = Pozice(HerniDeska.platno_hra, False, [421,509])
        HerniDeska.mapa_pozic[(5,4)] = Pozice(HerniDeska.platno_hra, False, [421,459])
        HerniDeska.mapa_pozic[(5,5)] = Pozice(HerniDeska.platno_hra, False, [421,409])


        HerniDeska.mapa_pozic[(6,1)] = Pozice(HerniDeska.platno_hra, False, [374,609])
        HerniDeska.mapa_pozic[(6,2)] = Pozice(HerniDeska.platno_hra, False, [374,559])
        HerniDeska.mapa_pozic[(6,3)] = Pozice(HerniDeska.platno_hra, False, [374,509])
        HerniDeska.mapa_pozic[(6,4)] = Pozice(HerniDeska.platno_hra, False, [374,459])
        HerniDeska.mapa_pozic[(6,5)] = Pozice(HerniDeska.platno_hra, False, [374,409])


        HerniDeska.mapa_pozic[(7,1)] = Pozice(HerniDeska.platno_hra, False, [294,609])
        HerniDeska.mapa_pozic[(7,2)] = Pozice(HerniDeska.platno_hra, False, [294,559])
        HerniDeska.mapa_pozic[(7,3)] = Pozice(HerniDeska.platno_hra, False, [294,509])
        HerniDeska.mapa_pozic[(7,4)] = Pozice(HerniDeska.platno_hra, False, [294,459])
        HerniDeska.mapa_pozic[(7,5)] = Pozice(HerniDeska.platno_hra, False, [294,409])

        HerniDeska.mapa_pozic[(8,1)] = Pozice(HerniDeska.platno_hra, False, [247,609])
        HerniDeska.mapa_pozic[(8,2)] = Pozice(HerniDeska.platno_hra, False, [247,559])
        HerniDeska.mapa_pozic[(8,3)] = Pozice(HerniDeska.platno_hra, False, [247,509])
        HerniDeska.mapa_pozic[(8,4)] = Pozice(HerniDeska.platno_hra, False, [247,459])
        HerniDeska.mapa_pozic[(8,5)] = Pozice(HerniDeska.platno_hra, False, [247,409])

        HerniDeska.mapa_pozic[(9,1)] = Pozice(HerniDeska.platno_hra, False, [200,609])
        HerniDeska.mapa_pozic[(9,2)] = Pozice(HerniDeska.platno_hra, False, [200,559])
        HerniDeska.mapa_pozic[(9,3)] = Pozice(HerniDeska.platno_hra, False, [200,509])
        HerniDeska.mapa_pozic[(9,4)] = Pozice(HerniDeska.platno_hra, False, [200,459])
        HerniDeska.mapa_pozic[(9,5)] = Pozice(HerniDeska.platno_hra, False, [200,409])

        HerniDeska.mapa_pozic[(10,1)] = Pozice(HerniDeska.platno_hra, False, [153,609])
        HerniDeska.mapa_pozic[(10,2)] = Pozice(HerniDeska.platno_hra, False, [153,559])
        HerniDeska.mapa_pozic[(10,3)] = Pozice(HerniDeska.platno_hra, False, [153,509])
        HerniDeska.mapa_pozic[(10,4)] = Pozice(HerniDeska.platno_hra, False, [153,459])
        HerniDeska.mapa_pozic[(10,5)] = Pozice(HerniDeska.platno_hra, False, [153,409])

        HerniDeska.mapa_pozic[(11,1)]= Pozice(HerniDeska.platno_hra, False, [106,609])
        HerniDeska.mapa_pozic[(11,2)] = Pozice(HerniDeska.platno_hra, False, [106,559])
        HerniDeska.mapa_pozic[(11,3)] = Pozice(HerniDeska.platno_hra, False, [106,509])
        HerniDeska.mapa_pozic[(11,4)] = Pozice(HerniDeska.platno_hra, False, [106,459])
        HerniDeska.mapa_pozic[(11,5)] = Pozice(HerniDeska.platno_hra, False, [106,409])

        HerniDeska.mapa_pozic[(12,1)] = Pozice(HerniDeska.platno_hra, False, [59,609])
        HerniDeska.mapa_pozic[(12,2)] = Pozice(HerniDeska.platno_hra, False, [59,559])
        HerniDeska.mapa_pozic[(12,3)] = Pozice(HerniDeska.platno_hra, False, [59,509])
        HerniDeska.mapa_pozic[(12,4)] = Pozice(HerniDeska.platno_hra, False, [59,459])
        HerniDeska.mapa_pozic[(12,5)] = Pozice(HerniDeska.platno_hra, False, [59,409])


        # horni pulka

        HerniDeska.mapa_pozic[(13,1)] = Pozice(HerniDeska.platno_hra, False, [610,59])
        HerniDeska.mapa_pozic[(13,2)] = Pozice(HerniDeska.platno_hra, False, [610,109])
        HerniDeska.mapa_pozic[(13,3)] = Pozice(HerniDeska.platno_hra, False, [610,159])
        HerniDeska.mapa_pozic[(13,4)] = Pozice(HerniDeska.platno_hra, False, [610,209])
        HerniDeska.mapa_pozic[(13,5)] = Pozice(HerniDeska.platno_hra, False, [610,259])

        HerniDeska.mapa_pozic[(14,1)] = Pozice(HerniDeska.platno_hra, False, [562,59])
        HerniDeska.mapa_pozic[(14,2)] = Pozice(HerniDeska.platno_hra, False, [562,109])
        HerniDeska.mapa_pozic[(14,3)] = Pozice(HerniDeska.platno_hra, False, [562,159])
        HerniDeska.mapa_pozic[(14,4)] = Pozice(HerniDeska.platno_hra, False, [562,209])
        HerniDeska.mapa_pozic[(14,5)] = Pozice(HerniDeska.platno_hra, False, [562,259])


        HerniDeska.mapa_pozic[(15,1)] = Pozice(HerniDeska.platno_hra, False, [515,59])
        HerniDeska.mapa_pozic[(15,2)] = Pozice(HerniDeska.platno_hra, False, [515,109])
        HerniDeska.mapa_pozic[(15,3)] = Pozice(HerniDeska.platno_hra, False, [515,159])
        HerniDeska.mapa_pozic[(15,4)] = Pozice(HerniDeska.platno_hra, False, [515,209])
        HerniDeska.mapa_pozic[(15,5)] = Pozice(HerniDeska.platno_hra, False, [515,259])

        HerniDeska.mapa_pozic[(16,1)] = Pozice(HerniDeska.platno_hra, False, [468,59])
        HerniDeska.mapa_pozic[(16,2)] = Pozice(HerniDeska.platno_hra, False, [468,109])
        HerniDeska.mapa_pozic[(16,3)] = Pozice(HerniDeska.platno_hra, False, [468,159])
        HerniDeska.mapa_pozic[(16,4)] = Pozice(HerniDeska.platno_hra, False, [468,209])
        HerniDeska.mapa_pozic[(16,5)] = Pozice(HerniDeska.platno_hra, False, [468,259])

        HerniDeska.mapa_pozic[(17,1)] = Pozice(HerniDeska.platno_hra, False, [421,59])
        HerniDeska.mapa_pozic[(17,2)] = Pozice(HerniDeska.platno_hra, False, [421,109])
        HerniDeska.mapa_pozic[(17,3)] = Pozice(HerniDeska.platno_hra, False, [421,159])
        HerniDeska.mapa_pozic[(17,4)] = Pozice(HerniDeska.platno_hra, False, [421,209])
        HerniDeska.mapa_pozic[(17,5)] = Pozice(HerniDeska.platno_hra, False, [421,259])


        HerniDeska.mapa_pozic[(18,1)] = Pozice(HerniDeska.platno_hra, False, [374,59])
        HerniDeska.mapa_pozic[(18,2)] = Pozice(HerniDeska.platno_hra, False, [374,109])
        HerniDeska.mapa_pozic[(18,3)] = Pozice(HerniDeska.platno_hra, False, [374,159])
        HerniDeska.mapa_pozic[(18,4)] = Pozice(HerniDeska.platno_hra, False, [374,209])
        HerniDeska.mapa_pozic[(18,5)] = Pozice(HerniDeska.platno_hra, False, [374,259])


        HerniDeska.mapa_pozic[(19,1)] = Pozice(HerniDeska.platno_hra, False, [294,59])
        HerniDeska.mapa_pozic[(19,2)] = Pozice(HerniDeska.platno_hra, False, [294,109])
        HerniDeska.mapa_pozic[(19,3)] = Pozice(HerniDeska.platno_hra, False, [294,159])
        HerniDeska.mapa_pozic[(19,4)] = Pozice(HerniDeska.platno_hra, False, [294,209])
        HerniDeska.mapa_pozic[(19,5)] = Pozice(HerniDeska.platno_hra, False, [294,259])

        HerniDeska.mapa_pozic[(20,1)] = Pozice(HerniDeska.platno_hra, False, [247,59])
        HerniDeska.mapa_pozic[(20,2)] = Pozice(HerniDeska.platno_hra, False, [247,109])
        HerniDeska.mapa_pozic[(20,3)] = Pozice(HerniDeska.platno_hra, False, [247,159])
        HerniDeska.mapa_pozic[(20,4)] = Pozice(HerniDeska.platno_hra, False, [247,209])
        HerniDeska.mapa_pozic[(20,5)] = Pozice(HerniDeska.platno_hra, False, [247,259])

        HerniDeska.mapa_pozic[(21,1)] = Pozice(HerniDeska.platno_hra, False, [200,59])
        HerniDeska.mapa_pozic[(21,2)] = Pozice(HerniDeska.platno_hra, False, [200,109])
        HerniDeska.mapa_pozic[(21,3)] = Pozice(HerniDeska.platno_hra, False, [200,159])
        HerniDeska.mapa_pozic[(21,4)] = Pozice(HerniDeska.platno_hra, False, [200,209])
        HerniDeska.mapa_pozic[(21,5)] = Pozice(HerniDeska.platno_hra, False, [200,259])

        HerniDeska.mapa_pozic[(22,1)] = Pozice(HerniDeska.platno_hra, False, [153,59])
        HerniDeska.mapa_pozic[(22,2)] = Pozice(HerniDeska.platno_hra, False, [153,109])
        HerniDeska.mapa_pozic[(22,3)] = Pozice(HerniDeska.platno_hra, False, [153,159])
        HerniDeska.mapa_pozic[(22,4)] = Pozice(HerniDeska.platno_hra, False, [153,209])
        HerniDeska.mapa_pozic[(22,5)] = Pozice(HerniDeska.platno_hra, False, [153,259])

        HerniDeska.mapa_pozic[(23,1)] = Pozice(HerniDeska.platno_hra, False, [106,59])
        HerniDeska.mapa_pozic[(23,2)] = Pozice(HerniDeska.platno_hra, False, [106,109])
        HerniDeska.mapa_pozic[(23,3)] = Pozice(HerniDeska.platno_hra, False, [106,159])
        HerniDeska.mapa_pozic[(23,4)] = Pozice(HerniDeska.platno_hra, False, [106,209])
        HerniDeska.mapa_pozic[(23,5)] = Pozice(HerniDeska.platno_hra, False, [106,259])

        HerniDeska.mapa_pozic[(24,1)] = Pozice(HerniDeska.platno_hra, False, [59,59])
        HerniDeska.mapa_pozic[(24,2)] = Pozice(HerniDeska.platno_hra, False, [59,109])
        HerniDeska.mapa_pozic[(24,3)] = Pozice(HerniDeska.platno_hra, False, [59,159])
        HerniDeska.mapa_pozic[(24,4)] = Pozice(HerniDeska.platno_hra, False, [59,209])
        HerniDeska.mapa_pozic[(24,5)] = Pozice(HerniDeska.platno_hra, False, [59,259])


class Dvojkostka:
    def __init__(self) -> None:
        pass

    def hod_dvojkostkou(self) -> list:
        prvni_hod = random.randint(1, 6)
        druhy_hod = random.randint(1, 6)
        if (prvni_hod == druhy_hod):
            return [prvni_hod for _ in range(4)]
        else:
            return [prvni_hod, druhy_hod]


if __name__ == "__main__":
    app = Hra(root)
    root.mainloop()
