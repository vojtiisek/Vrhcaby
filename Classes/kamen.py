class Kamen:
    def __init__(self, barva_kamene: str, pozice_kamene: int) -> None:
        self._barva_kamene = barva_kamene
        self._pozice_kamene = pozice_kamene
        self._historie = []

    @property
    def barva_kamene(self) -> str:
        return self._barva_kamene

    @property
    def historie(self) -> list:
        return self._historie

    @property
    def pozice_kamene(self) -> int:
        return self._pozice_kamene

    @pozice_kamene.setter
    def pozice_kamene(self, nova_pozice_kamene: int) -> None:
        if self._pozice_kamene != nova_pozice_kamene:
            self.pridej_pozici_do_historie()
            self._pozice_kamene = nova_pozice_kamene

    def pridej_pozici_do_historie(self) -> None:
        self.historie.append(self.pozice_kamene)

    def __str__(self) -> str:
        return f"Tento {self.barva_kamene} kamen je na pozici {self.pozice_kamene}"
