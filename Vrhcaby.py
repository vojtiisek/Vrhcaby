import tkinter as tk
from tkinter import *
from tkinter import messagebox, Message
from PIL import ImageTk, Image 
from pathlib import Path

class HerniDeska:
    def __init__(self, hra) -> None:

        # Okno
        self.hra = hra
        self.hra.resizable(False, False)
        self.hra.geometry("964x669")
        self.hra.title("Vrhcaby")

        # Pozadi menu
        self.pozadi_obrazek = Image.open("wooden_table_background.jpg")
        self.pozadi_menu = ImageTk.PhotoImage(self.pozadi_obrazek)

        # Platno - menu
        self.platno_menu = tk.Canvas(self.hra, width=964, height=669)  
        self.platno_menu.create_image(0,0,image=self.pozadi_menu, anchor=tk.NW)
        self.platno_menu.pack()

        # Ikona
        icon = Image.open("vrhcaby_icon.png")
        icon_tk = ImageTk.PhotoImage(icon)
        self.hra.wm_iconphoto(False, icon_tk)

        # Tlacitka
        # Tlacitko "Hrat"
        self.start_game_bg = Image.open("start_button.png") 
        self.start_game_bg_tk = ImageTk.PhotoImage(self.start_game_bg)
        self.start_game_button = Button(self.platno_menu, image=self.start_game_bg_tk, command=lambda : self.hrat_button_click(), bd=0, highlightthickness=0)
        self.start_game_button.config(width=self.start_game_bg_tk.width(), height=self.start_game_bg_tk.height())
        self.platno_menu.create_window(480, 300, window=self.start_game_button)

        # Tlacitko "Pokracovat"
        self.continue_game_bg = Image.open("continue_button.png") 
        self.continue_game_bg_tk = ImageTk.PhotoImage(self.continue_game_bg)
        self.continue_game_bg_button = Button(self.platno_menu, image=self.continue_game_bg_tk, bd=0, highlightthickness=0)
        self.continue_game_bg_button.config(width=self.continue_game_bg_tk.width(), height=self.continue_game_bg_tk.height())
        self.platno_menu.create_window(480, 430, window=self.continue_game_bg_button)
       

        # Tlacitko "Ukoncit hru"
        self.quit_game_bg = Image.open("quit_game_button.png") 
        self.quit_game_bg_tk = ImageTk.PhotoImage(self.quit_game_bg)
        self.quit_game_bg_button = Button(self.platno_menu, image=self.quit_game_bg_tk, command=lambda : self.ukoncit_hru(), bd=0, highlightthickness=0)
        self.quit_game_bg_button.config(width=self.quit_game_bg_tk.width(), height=self.quit_game_bg_tk.height())
        self.platno_menu.create_window(480, 560, window=self.quit_game_bg_button)




        # Pozadi - hra
        self.pozadi_obrazek_hra = Image.open("vrhcaby_mapa.jpg")
        self.pozadi_hra = ImageTk.PhotoImage(self.pozadi_obrazek_hra)

        # Platno - hra
        self.platno_hra = tk.Canvas(self.hra, width=964, height=669)  
        self.platno_hra.create_image(0,0,image=self.pozadi_hra, anchor=tk.NW)
        self.platno_hra.pack_forget()
        self.pridej_kameny()

    def pridej_kameny(self):
        pass

    def vytvor_pointy(self):
        point1 = Zasobnik(self, 15)
        point2 = Zasobnik(self, 15)
        point3 = Zasobnik(self, 15)
        point4 = Zasobnik(self, 15)
        point5 = Zasobnik(self, 15)
        point6 = Zasobnik(self, 15)
        point7 = Zasobnik(self, 15)
        point8 = Zasobnik(self, 15)
        point9 = Zasobnik(self, 15)
        point10 = Zasobnik(self, 15)
        point11 = Zasobnik(self, 15)
        point12 = Zasobnik(self, 15)
        point13 = Zasobnik(self, 15)
        point14 = Zasobnik(self, 15)
        point15 = Zasobnik(self, 15)
        point16 = Zasobnik(self, 15)
        point17 = Zasobnik(self, 15)
        point18 = Zasobnik(self, 15)
        point19 = Zasobnik(self, 15)
        point20 = Zasobnik(self, 15)
        point21 = Zasobnik(self, 15)
        point22 = Zasobnik(self, 15)
        point23 = Zasobnik(self, 15)
        point24 = Zasobnik(self, 15)

    def hrat_button_click(self):
        self.shovej_menu()
        self.vykresli_hraci_desku()

    def ukoncit_hru(self):
        self.hra.destroy()

    def start(self):
        self.hra.mainloop()
    
    def vykresli_hraci_desku(self):
        self.platno_hra.pack()
    
    def shovej_menu(self):
        self.platno_menu.pack_forget()

class Zasobnik:
    def __init__(self, max_size : int):
        self.zasobnik = []
        self.max_size = max_size

    def push(self, item) -> None:
        if(self.size >= self.max_size):
            pass
        else: 
            self.zasobnik.append(item)
  
    def pop(self) -> None:
        if(len(self.zasobnik) > 0):
            self.zasobnik.pop(-1)
        else:
            pass

    def front(self):
        if(len(self.zasobnik) > 0):
            return self.zasobnik[0]
        else:
            pass
  
    def rear(self):
        if(len(self.zasobnik) > 0):
            return self.zasobnik[len(self.zasobnik)-1]
        else:
            pass
  
    def is_empty(self) -> bool:
        if(len(self.zasobnik) <= 0):
            return True
        else:
            return False

    def size(self) -> int:
        return len(self.zasobnik)

class Hra:
    def __init__(self, hra):
        self.hra = hra
        self.platno = HerniDeska(self.hra)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Hra(root)
    root.mainloop()
