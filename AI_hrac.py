from Hrac import Hrac

class AI_Hrac(Hrac):
    def __init__(self, barva : str) -> None:
        self._barva = barva
        self._vysledky_dvojkostky = []
        self._mozne_tahy = []
        self._prvni_hod = 0
        self._pocet_hozenych_cisel = 0
        self._odehrane_kameny = []
        self._aktualni_pointy = []
        self._statistiky = {
            "pocet_vyvedenych_kamenu" : 0,
            "pocet_vyhozenych_kamenu" : 0,
            "pocet_vyhozenych_svych_kamenu" : 0,
            "prumerna_zivotnost_kamene" : 0.0} 

    @property
    def get_barva(self):
        return self._barva
              
    def set_barva(self, value : str):
        self._barva = value

    @property
    def get_vysledky(self):
        return self._vysledky_dvojkostky    
   
    def set_vysledky(self, values : list):
        self._vysledky_dvojkostky = values

    @property
    def get_statistiky(self):
        return self._statistiky  

    @property
    def get_mozne_tahy(self):
        return self._mozne_tahy
      
    def set_mozne_tahy(self, values : list):
        self._mozne_tahy = values

    @property
    def get_prvni_hod(self) -> int:
        return self._prvni_hod
      
    def set_prvni_hod(self, value : int):
        self._prvni_hod = value

    @property
    def get_hozeny_pocet(self) -> int:
        return self._pocet_hozenych_cisel
      
    def set_hozeny_pocet(self, value : int):
        self._pocet_hozenych_cisel = value

    @property
    def get_odehrane_kameny(self) -> list:
        return self._odehrane_kameny

    @property
    def get_aktualni_pointy(self) -> list:
        return self._aktualni_pointy

    def set_aktualni_pointy(self, value):
        self._aktualni_pointy = value

