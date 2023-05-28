import random
from StavHry import StavHry
from Label_manager import Label_manager

class Dvojkostka:

    def hod_dvojkostkou() -> list:

        prvni_hod = random.randint(1, 6)
        druhy_hod = random.randint(1, 6)
        if (prvni_hod == druhy_hod):
            print([prvni_hod for _ in range(4)])
            return [prvni_hod for _ in range(4)]
        else:
            print([prvni_hod, druhy_hod])
            return [prvni_hod, druhy_hod]

    def rozehrat():
        hraci = StavHry.get_hraci()
        if StavHry.get_stav() == "hrac1_kostka":
            hraci["Hrac1"].set_prvni_hod(random.randint(1, 6))
            StavHry.set_stav("hrac2_kostka")
            
        elif StavHry.get_stav() == "hrac2_kostka":
            hraci["Hrac2"].set_prvni_hod(random.randint(1, 6))
            if(hraci["Hrac2"].get_prvni_hod == hraci["Hrac1"].get_prvni_hod):
                Dvojkostka.rozehrat()
        
        if(hraci["Hrac1"].get_prvni_hod > 0 and hraci["Hrac2"].get_prvni_hod > 0):
            if hraci["Hrac1"].get_prvni_hod > hraci["Hrac2"].get_prvni_hod:
                StavHry.set_stav("Hrac1")
            else:
                StavHry.set_stav("Hrac2")

