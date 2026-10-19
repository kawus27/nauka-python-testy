def sprawdz_wiek(wiek):
    if wiek > 120:
        return "Nierealny wiek"
    elif wiek >= 18:
        return "Pełnoletni"
    elif wiek < 0:
        return "Przyszłość"
    else:
        return "Niepełnoletni"

assert sprawdz_wiek(-4) == "Przyszłość"
assert sprawdz_wiek(18) == "Pełnoletni"
assert sprawdz_wiek(17) == "Niepełnoletni"
assert sprawdz_wiek(32) == "Pełnoletni"
assert sprawdz_wiek(120) == "Pełnoletni"
assert sprawdz_wiek(121) == "Nierealny wiek"
assert sprawdz_wiek(226) == "Nierealny wiek"