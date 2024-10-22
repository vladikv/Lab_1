dystans = input("Podaj drogę pokonaną przez samochód (w kilometrach): ")
spalanie_na_100_km = input("Podaj średnie spalanie samochodu (w litrach na 100 km): ")

cena_paliwa = 6.5  # zł/litr

zuzycie_paliwa = (dystans * spalanie_na_100_km) / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print(f"\nPrzewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")