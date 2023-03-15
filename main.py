from firma import Firma
from pracownik import Pracownik

firma = Firma ("XD")

pracownik1= Pracownik("Adam", "Kowalski", 23, "Junior", 0.5, 0)
pracownik2= Pracownik("Bartek", "Niebieski", 25, "Mid", 2, 0)
pracownik3= Pracownik("Krystian", "Sosna", 34, "Senior", 5, 0)
pracownik4= Pracownik("Karol", "Krowa", 34, "Szef", 5, 0)

firma.dodaj_pracownika(pracownik1)
firma.dodaj_pracownika(pracownik3)
firma.dodaj_pracownika(pracownik2)

for pracownik in firma.pracownicy:
    print (pracownik.oblicz_zarobki())



