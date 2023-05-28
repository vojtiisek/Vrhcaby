class StavHry:
    _stav = ""
    _hraci = {}

    def set_stav(value : str):
        StavHry._stav = value
        print(f"Novy stav input: {value}, nastaveny stav: {StavHry._stav}")

    def get_stav():
        return StavHry._stav

    def add_hrac(nick, hrac):
        StavHry._hraci[nick] = hrac

    def get_hraci():
        return StavHry._hraci