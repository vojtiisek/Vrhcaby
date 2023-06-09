import random
from StavHry import StavHry
from Label_manager import Label_manager

class Dvojkostka:
    zvoleny_souper = ""
    def hod_dvojkostkou() -> list:

        vysledek_hodu = []
        prvni_hod = random.randint(1, 6)
        druhy_hod = random.randint(1, 6)
        if (prvni_hod == druhy_hod):
            vysledek_hodu = [prvni_hod for _ in range(4)]
        else:
            vysledek_hodu = [prvni_hod, druhy_hod]
        
        return vysledek_hodu

    def rozehrat(platno):
        hraci = StavHry.get_hraci()

        if StavHry.get_stav() == "hrac1_kostka":
            hraci["Hrac1"].set_prvni_hod(random.randint(1, 6))
            if Dvojkostka.zvoleny_souper == "AI":
                hraci["Hrac2"].set_prvni_hod(random.randint(1, 6))

        if StavHry.get_stav() == "hrac2_kostka":
            hraci["Hrac2"].set_prvni_hod(random.randint(1, 6))
            if(hraci["Hrac2"].get_prvni_hod == hraci["Hrac1"].get_prvni_hod):
                Dvojkostka.rozehrat(platno)

        stav_hrac = ""
        if(StavHry.get_stav() == "hrac1_kostka"):
            stav_hrac = "Hrac1"
        else:
            stav_hrac = "Hrac2"

        

        Label_manager.zobraz_vysledky_dvojkostky(platno, hraci[stav_hrac].get_barva, [hraci[stav_hrac].get_prvni_hod])
        if Dvojkostka.zvoleny_souper == "AI":
            Label_manager.zobraz_vysledky_dvojkostky(platno, hraci["Hrac2"].get_barva, [hraci["Hrac2"].get_prvni_hod])

        if StavHry.get_stav() == "hrac1_kostka":
            if Dvojkostka.zvoleny_souper == "AI":
                ... # rozhodne se v bloku kodu pod timto
            else:
                StavHry.set_stav("hrac2_kostka")           
        
        if(hraci["Hrac1"].get_prvni_hod > 0 and hraci["Hrac2"].get_prvni_hod > 0):
            if hraci["Hrac1"].get_prvni_hod > hraci["Hrac2"].get_prvni_hod:
                StavHry.set_stav("Hrac1")
            else:
                StavHry.set_stav("Hrac2")

