class Pracownik:
    def __init__(self, imie, nazwisko, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.zarobki = zarobki
    def say(self):
        print(f"Ten pracownik nazywa sie {self.imie} {self.nazwisko} oraz zarabia {self.zarobki}")

pracownik1 = Pracownik ("Adam", "Kowalski", 4000)

pracownik1.say()
