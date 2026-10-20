from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.nazwa_produktu = page.locator("[data-test='cart-list'] [data-test='inventory-item-name']")