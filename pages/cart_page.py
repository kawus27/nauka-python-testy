from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.lista_produktow = page.locator("[data-test='cart-list']")
        self.nazwa_produktu = page.locator("[data-test='cart-list'] [data-test='inventory-item-name']")

    def poczekaj_na_zaladowanie(self):
        self.lista_produktow.wait_for()