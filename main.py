class Pracownik:
    def __init__(self, imie, nazwisko, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.zarobki = zarobki
    def say(self):
        print(f"Ten pracownik nazywa sie {self.imie} {self.nazwisko} oraz zarabia {self.zarobki}")
    def podwyzka(self, wartoscpodwyzki):
        self.zarobki = self.zarobki + wartoscpodwyzki
        print(f"Pracownik {self.imie} po podwyżce zarabia {self.zarobki}")



pracownik1 = Pracownik ("Adam", "Kowalski", 4000)
pracownik2 = Pracownik ("Bartek", "zzz", 7000)
pracownik3 = Pracownik ("Piotr", "Malecki", 1000)

pracownik1.say()
pracownik1.podwyzka(500)

pracownik2.say()
pracownik2.podwyzka(420)

pracownik3.say()
pracownik3.podwyzka(325)

