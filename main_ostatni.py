from faker import Faker
import random
fake = Faker()
stanowisko= ["Junior", "Mid", "Senior", "Szef"]
pracownicy = []
for y in range(100):
    pracownik ={ 'imie': fake.first_name(),'nazwisko': fake.last_name(),'zarobki': random.randint(2000, 10000),'pozycja': random.choice(stanowisko)}
    pracownicy.append(pracownik)

ponizej_5000 = [x for x in pracownicy if x['zarobki'] < 5000]

juniorzy = [x['imie'] for x in pracownicy if x ['pozycja'] == "Junior"]

print("Osoby z zarobkami mnieszymi niz 5000: " )
for x in ponizej_5000:
    print(x['imie'] , x['nazwisko'])

print("Osoby ze stanowiskiem juniora: ")
for nazwisko in juniorzy:
    print(nazwisko)