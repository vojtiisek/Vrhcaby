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

    @classmethod
    def vytvor_pointy(cls):
        # 5 - maximalni pocet kamenu na danem pointu (z duvodu mista na mape vyuzivame tzv. Egyptian rule)
        zasobniky = []
        for i in range(1, 24+1):
            zasobniky.append(Zasobnik(5))
        print(zasobniky[0])
        print(zasobniky[1])
        return zasobniky

    #@classmethod
    #def pridej_pozice(cls):  # naplni vsechny pointy maximalnim poctem kamenu (5ti) - tyto kameny jsou skryte a pouzivane pro posuny a pro napovedu dalsich tahu
    pozice1_1 = Pozice(platno_hra, False, [610,609])
    pozice1_2 = Pozice(platno_hra, False, [610,559])
    pozice1_3 = Pozice(platno_hra, False, [610,509])
    pozice1_4 = Pozice(platno_hra, False, [610,459])
    pozice1_5 = Pozice(platno_hra, False, [610,409])

    pozice2_1 = Pozice(platno_hra, False, [562,609])
    pozice2_2 = Pozice(platno_hra, False, [562,559])
    pozice2_3 = Pozice(platno_hra, False, [562,509])
    pozice2_4 = Pozice(platno_hra, False, [562,459])
    pozice2_5 = Pozice(platno_hra, False, [562,409])


    pozice3_1 = Pozice(platno_hra, False, [515,609])
    pozice3_2 = Pozice(platno_hra, False, [515,559])
    pozice3_3 = Pozice(platno_hra, False, [515,509])
    pozice3_4 = Pozice(platno_hra, False, [515,459])
    pozice3_5 = Pozice(platno_hra, False, [515,409])

    pozice4_1 = Pozice(platno_hra, False, [468,609])
    pozice4_2 = Pozice(platno_hra, False, [468,559])
    pozice4_3 = Pozice(platno_hra, False, [468,509])
    pozice4_4 = Pozice(platno_hra, False, [468,459])
    pozice4_5 = Pozice(platno_hra, False, [468,409])

    pozice5_1 = Pozice(platno_hra, False, [421,609])
    pozice5_2 = Pozice(platno_hra, False, [421,559])
    pozice5_3 = Pozice(platno_hra, False, [421,509])
    pozice5_4 = Pozice(platno_hra, False, [421,459])
    pozice5_5 = Pozice(platno_hra, False, [421,409])


    pozice6_1 = Pozice(platno_hra, False, [374,609])
    pozice6_2 = Pozice(platno_hra, False, [374,559])
    pozice6_3 = Pozice(platno_hra, False, [374,509])
    pozice6_4 = Pozice(platno_hra, False, [374,459])
    pozice6_5 = Pozice(platno_hra, False, [374,409])


    pozice7_1 = Pozice(platno_hra, False, [294,609])
    pozice7_2 = Pozice(platno_hra, False, [294,559])
    pozice7_3 = Pozice(platno_hra, False, [294,509])
    pozice7_4 = Pozice(platno_hra, False, [294,459])
    pozice7_5 = Pozice(platno_hra, False, [294,409])

    pozice8_1 = Pozice(platno_hra, False, [247,609])
    pozice8_2 = Pozice(platno_hra, False, [247,559])
    pozice8_3 = Pozice(platno_hra, False, [247,509])
    pozice8_4 = Pozice(platno_hra, False, [247,459])
    pozice8_5 = Pozice(platno_hra, False, [247,409])

    pozice9_1 = Pozice(platno_hra, False, [200,609])
    pozice9_2 = Pozice(platno_hra, False, [200,559])
    pozice9_3 = Pozice(platno_hra, False, [200,509])
    pozice9_4 = Pozice(platno_hra, False, [200,459])
    pozice9_5 = Pozice(platno_hra, False, [200,409])

    pozice10_1 = Pozice(platno_hra, False, [153,609])
    pozice10_2 = Pozice(platno_hra, False, [153,559])
    pozice10_3 = Pozice(platno_hra, False, [153,509])
    pozice10_4 = Pozice(platno_hra, False, [153,459])
    pozice10_5 = Pozice(platno_hra, False, [153,409])


    @classmethod
    def pridej_kameny(cls):
        pass

    @classmethod
    def hrat_button_click(cls):
        HerniDeska.shovej_menu()
        HerniDeska.vykresli_hraci_desku()

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
