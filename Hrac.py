from abc import ABC, abstractmethod

class Hrac(ABC):
    def __init__(self, barva : str) -> None:
        self._barva = barva
        self._vysledky_dvojkostky = []
        self._mozne_tahy = []
        self._prvni_hod = 0

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
    def get_mozne_tahy(self):
        return self._mozne_tahy
      
    def set_mozne_tahy(self, values : list):
        self._mozne_tahy = values

    @property
    def get_prvni_hod(self) -> int:
        return self._prvni_hod
      
    def set_prvni_hod(self, value : int):
        self._prvni_hod = value

