class Pracownik:
    def __init__ (self, imie, nazwisko, wiek, stanowisko, doswiadzczenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek= wiek
        self.stanowisko = stanowisko
        self.doswiadzczenie = doswiadzczenie
def oblicz_zarobki(self):
    if self.doswiadzczenie < 1:
        return 2000
    elif 1< self.doswiadzczenie < 3:
        return 5000
    else:
        return 10000