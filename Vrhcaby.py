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
    #HerniDeska.pridej_kameny()

    kaminek = Herni_kamen(platno_hra, "bila",[0,0])
    pozicka = Pozice(platno_hra, False, kaminek, [0,0])

    @classmethod
    def pridej_kameny(cls):
        pass

    @classmethod
    def vytvor_pointy(cls):
        # 5 - maximalni pocet kamenu na danem pointu (z duvodu mista na mape vyuzivame tzv. Egyptian rule)
        zasobniky = []
        for i in range(1, 24+1):
            zasobniky.append(Zasobnik(5))
        return zasobniky

    @classmethod
    def pridej_pozice(cls):  # naplni vsechny pointy maximalnim poctem kamenu (5ti) - tyto kameny jsou skryte a pouzivane pro posuny a pro napovedu dalsich tahu
        kamen1_0 = Pozice(HerniDeska.platno_hra, False, None, [100, 100])

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
