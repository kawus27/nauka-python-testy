from playwright.sync_api import Page, expect
from pages.login_page import LoginPage, BASE_URL
from pages.cart_page import CartPage

def test_tytul_strony(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Swag Labs")


def test_poprawne_logowanie(page: Page):
    login_page = LoginPage(page)
    login_page.otworz()
    login_page.zaloguj("standard_user", "secret_sauce")
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")

def test_zle_haslo(page: Page):
    login_page = LoginPage(page)
    login_page.otworz()
    login_page.zaloguj("standard_user", "zlehaslo")
    expect(login_page.komunikat_bledu).to_contain_text("Username and password do not match")

def test_zablokowany_uzytkownik(page: Page):
    login_page = LoginPage(page)
    login_page.otworz()
    login_page.zaloguj("locked_out_user", "secret_sauce")
    expect(login_page.komunikat_bledu).to_contain_text("this user has been locked out")


def test_dodanie_do_koszyka(strona_produktow):
    inventory_page = strona_produktow
    expect(inventory_page.tytul_strony).to_have_text("Products")
    inventory_page.dodaj_plecak_do_koszyka()
    expect(inventory_page.koszyk_licznik).to_have_text("1")

def test_plecak_w_koszyku(page: Page, strona_produktow):
    inventory_page = strona_produktow
    inventory_page.dodaj_plecak_do_koszyka()
    inventory_page.przejdz_do_koszyka()
    cart_page = CartPage(page)
    expect(cart_page.nazwa_produktu).to_have_text("Sauce Labs Backpack")
