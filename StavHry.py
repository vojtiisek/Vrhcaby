class StavHry:
    _stav = ""
    _hraci = {}

    def set_stav(value : str):
        print(f"New stav: {value}")
        StavHry._stav = value

    def get_stav():
        return StavHry._stav

    def add_hrac(nick, hrac):
        StavHry._hraci[nick] = hrac

    def get_hraci():
        return StavHry._hraci