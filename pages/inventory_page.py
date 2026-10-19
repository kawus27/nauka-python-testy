from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.przycisk_dodaj_plecak = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.koszyk_licznik = page.locator("[data-test='shopping-cart-badge']")
        self.tytul_strony = page.locator("[data-test='title']")

    def dodaj_plecak_do_koszyka(self):
        self.przycisk_dodaj_plecak.click()