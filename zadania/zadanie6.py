from wiek import sprawdz_wiek

lista_wiekow = [15, 18, 34, -2, 130, 17 , 45, 0]

full_age = 0
unplausible = 0
not_full_age = 0
for wiek in lista_wiekow:
    wynik = sprawdz_wiek(wiek)
    print(wiek, "->", wynik)
    if wynik == "Pełnoletni":
        full_age += 1
    elif wynik == "Nierealny wiek":
        unplausible += 1
    elif wynik == "Przyszłość":
        unplausible += 1
    elif wynik == "Niepełnoletni":
        not_full_age += 1

print("Pełnoletnich:", full_age)
print("Nierealnych:", unplausible)
print("Niepełnoletnich:", not_full_age)