import pytest
from wiek import sprawdz_wiek

@pytest.mark.parametrize("wiek, oczekiwany", [
    pytest.param(-4, "Przyszłość", id="rok_z_przyszlosci"),
    pytest.param(18, "Pełnoletni", id="dokladnie_18"),
    pytest.param(17, "Niepełnoletni", id="tuz_przed_granica_18"),
    pytest.param(0, "Niepełnoletni", id="noworodek"),
    pytest.param(32, "Pełnoletni", id="pelnoletni"),
    pytest.param(120, "Pełnoletni", id="granica_120"),
    pytest.param(121, "Nierealny wiek", id="tuz_za_granica_120"),
    pytest.param(226, "Nierealny wiek", id="grubo_za_granica_120"),
])

def test_sprawdz_wiek(wiek, oczekiwany):
    assert sprawdz_wiek(wiek) == oczekiwany