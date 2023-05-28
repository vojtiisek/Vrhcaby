import random
from StavHry import StavHry

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
            hraci["hrac1"].set_prvni_hod(random.randint(1, 6))
        elif StavHry.get_stav() == "hrac2_kostka":
            hraci["hrac2"].set_prvni_hod(random.randint(1, 6))
