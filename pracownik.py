class Pracownik:
    def __init__(self, imie, nazwisko, wiek, stanowisko, doswiadzczenie, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.stanowisko = stanowisko
        self.doswiadzczenie = doswiadzczenie
        self.zarobki = zarobki

    def oblicz_zarobki(self):
        if self.doswiadzczenie < 1:
            return self.zarobki + 2000
        elif 1 < self.doswiadzczenie < 3:
            return self.zarobki + 5000
        else:
            return self.zarobki + 10000
