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
    def awansuj_pracownika (self,pracownik):
        for pracownik in self.pracownicy:
            if pracownik.firmy.imie == pracownik.imie and pracownik.firmy.nazwisko == pracownik.nazwisko
                if pracownik.stanowisko == "Junior":
                    pracownik.stanowisko = "Mid"

                elif pracownik.stanowisko == "Mid":
                    pracownik.stanowisko = "Senior"

                elif pracownik.stanowisko == "Senior":
                    pracownik.stanoiwsko = "Szef"
                pracownik.zarobki += 500