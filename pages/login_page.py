from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.pole_login = page.locator("[data-test='username']")
        self.pole_haslo = page.locator("[data-test='password']")
        self.przycisk_login = page.locator("[data-test='login-button']")
        self.komunikat_bledu = page.locator("[data-test='error']")

    def otworz(self):
        self.page.goto(BASE_URL)

    def zaloguj(self, login, haslo):
        self.pole_login.fill(login)
        self.pole_haslo.fill(haslo)
        self.przycisk_login.click()