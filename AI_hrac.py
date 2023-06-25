from Hrac import Hrac

class AI_Hrac(Hrac):
    def __init__(self, barva) -> None:
        super().__init__(barva)
        self._aktualni_pointy = []

    @property
    def get_aktualni_pointy(self) -> list:
        return self._aktualni_pointy

    def set_aktualni_pointy(self, value):
        self._aktualni_pointy = value

