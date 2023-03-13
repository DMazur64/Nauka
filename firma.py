class Firma:
    def __init__ (self, nazwa):
        self.nazwa = nazwa
        self.pracownicy = []
    def dodaj_pracownika (self, pracownik):
        self.pracownicy.append(pracownik)
    def liczba_pracownikow (self):
        return len(self.pracownicy)
    def usun_pracownika(self, pracownik):
        self.pracownicy.remove(pracownik)
    def laczne_zarobki (self):
        sum = 0
        for pracownik in self.pracownicy:
            sum += pracownik.zarobki
        return sum
