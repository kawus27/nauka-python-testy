import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def uzytkownik_1():
    return requests.get(f"{BASE_URL}/users/1")

def test_status_uzytkownika(uzytkownik_1):
    assert uzytkownik_1.status_code == 200

def test_dane_uzytkownika(uzytkownik_1):
    
    dane = uzytkownik_1.json()
    assert dane["name"] == "Leanne Graham"
    assert dane["username"] == "Bret"

def test_liczba_uzytkownikow():
    odpowiedz = requests.get(f"{BASE_URL}/users")
    assert len(odpowiedz.json()) == 10

def test_nieistniejacy_uzytkownik():
    odpowiedz = requests.get(f"{BASE_URL}/users/999")
    assert odpowiedz.status_code == 404

def test_tworzenie_posta():
    nowy_post = {"title": "Test", "body": "Treść", "userId": 1}
    odpowiedz = requests.post(f"{BASE_URL}/posts", json=nowy_post)
    assert odpowiedz.status_code == 201
    dane = odpowiedz.json()
    assert dane["title"] == "Test"