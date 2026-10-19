import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_status_uzytkownika():
    odpowiedz = requests.get(f"{BASE_URL}/users/1")
    assert odpowiedz.status_code == 200

def test_dane_uzytkownika():
    odpowiedz = requests.get(f"{BASE_URL}/users/1")
    dane = odpowiedz.json()
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
    dane = odpowiedz.json()
    assert odpowiedz.status_code == 201
    assert dane["title"] == "Test"