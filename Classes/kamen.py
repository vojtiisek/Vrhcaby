class Kamen:
    def __init__(self, barva_kamene: str) -> None:
        self.barva_kamene = barva_kamene
        self.historie = []

    @property
    def barva_kamene(self) -> str:
        return self.barva_kamene

    @property
    def historie(self) -> list:
        return self.historie

    def pridej_pozici_do_historie(self, nova_pozice_kamene: int):
        self.historie.append(nova_pozice_kamene)

    def __str__(self) -> str:
        return f"Tento {self.barva_kamene} kámen je na pozici {self.historie[-1]}"
