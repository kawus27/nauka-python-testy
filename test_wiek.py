from wiek import sprawdz_wiek

def test_wiek_ujemny():
    assert sprawdz_wiek(-4) == "Przyszłość"

def test_dokladnie_18():
    assert sprawdz_wiek(18) == "Pełnoletni"

def test_17_lat():
    assert sprawdz_wiek(17) == "Niepełnoletni"

def test_0_lat():
    assert sprawdz_wiek(0) == "Niepełnoletni"

def test_pelnoletni():
    assert sprawdz_wiek(32) == "Pełnoletni"

def test_granica_120():
    assert sprawdz_wiek(120) == "Pełnoletni"

def test_nad_granica_121():
    assert sprawdz_wiek(121) == "Nierealny wiek"

def test_grubo_nad_226():
    assert sprawdz_wiek(226) == "Nierealny wiek"