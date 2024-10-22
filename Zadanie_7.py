import random

spalanie_na_100_km = float(input("Podaj średnie spalanie samochodu (w litrach na 100 km): "))

dystans = random.randint(50, 500)

cena_paliwa = 6.5

zuzycie_paliwa = (dystans * spalanie_na_100_km) / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print(f"\nWygenerowana losowa długość trasy: {dystans} km")
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")