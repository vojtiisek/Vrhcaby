class Mapa_pozic():
    _mapa_pozic = {} # { (point, vyska) : Pozice() } ; napø. { [1,1] : pozice1_1 }
    
    @staticmethod
    def get_mapa_pozic() -> dict:
        return Mapa_pozic._mapa_pozic