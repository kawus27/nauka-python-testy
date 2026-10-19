def sprawdz_wiek(wiek):
    if wiek > 120:
        return "Nierealny wiek"
    elif wiek >= 18:
        return "Pełnoletni"
    elif wiek < 0:
        return "Przyszłość"
    else:
        return "Niepełnoletni"