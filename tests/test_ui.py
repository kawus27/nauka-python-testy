from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"

def zaloguj(page: Page, login, haslo):
    page.goto(BASE_URL)
    page.locator("[data-test='username']").fill(login)
    page.locator("[data-test='password']").fill(haslo)
    page.locator("[data-test='login-button']").click()

def test_tytul_strony(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Swag Labs")


def test_poprawne_logowanie(page: Page):
    zaloguj(page, "standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='title']")).to_have_text("Products")

def test_zle_haslo(page: Page):
    zaloguj(page, "standard_user", "zlehaslo")
    expect(page.locator("[data-test='error']")).to_contain_text("Username and password do not match")

def test_zablokowany_uzytkownik(page: Page):
    zaloguj(page, "locked_out_user", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("this user has been locked out")