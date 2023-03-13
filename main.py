import pracownik
from firma import Firma
from pracownik import Pracownik

firma = Firma("XD")

pracownik1= Pracownik("Adam", "Kowalski", 23, "Junior", 0.5)
pracownik2= Pracownik("Bartek", "Niebieski", 25, "Mid", 2)
pracownik3= Pracownik("Krystian", "Sosna", 34, "Senior", 5)

firma.dodaj_pracownika(pracownik1)
firma.dodaj_pracownika(pracownik3)
firma.dodaj_pracownika(pracownik2)

print (f"{pracownik.oblicz_zarobki(pracownik1)}")
print (f"{pracownik.oblicz_zarobki(pracownik2)}")
print (f"{pracownik.oblicz_zarobki(pracownik3)}")