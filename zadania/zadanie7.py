from wiek import sprawdz_wiek
from datetime import date

while True:
    try:
        rok = int(input("Podaj rok urodzenia: "))
    except ValueError:
        print("To nie jest liczba, spróbuj ponownie")
        continue

    wiek = date.today().year - rok
    wynik = sprawdz_wiek(wiek)
    if wynik in ["Pełnoletni", "Niepełnoletni"]:
        break
    print("Niepoprawny rok: ", wynik)

print(wiek, "->", wynik)
