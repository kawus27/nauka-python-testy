imie = input("Podaj imię: ")
rok = int(input("Podaj rok urodzenia: "))
wiek = 2026 - rok

if wiek > 120:
    print("Błąd: Nierealny wiek")
elif wiek >= 18:
    print("Nazywasz się", imie, "i masz", wiek, "lat")
    print("Jesteś pełnoletni")
elif wiek < 0:
    print("Błąd: rok urodzenia z przyszłości")
else:
    print("Nazywasz się", imie, "i masz", wiek, "lat")
    print("Jesteś niepełnoletni")