from zwierze import Zwierze, Ptak

imiona = ["Adam", "Bartek", "Dawid", "Mateusz", "Artur", "Krystian", "Kuba", "Antek", "Zbyszek", "Oskar"]
for i in range(1):
    print(imiona)
print()
for imie in imiona:
    print(imie)
print()
for imie in imiona:
    if imie.startswith("A"):
        print(imie)
print()
try:
    print(5/0)
except Exception:
    print ("Nie mozna dzielic przez 0")

print()

zwierze1= Zwierze(12, "Krowa", "Gospodarstwo")
ptak1= Ptak (4, "Orzeł", "Las", "Brązowy")

print(zwierze1.say())
print(ptak1.say())