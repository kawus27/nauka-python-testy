import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def strona_produktow(page: Page):
    login_page = LoginPage(page)
    login_page.otworz()
    login_page.zaloguj("standard_user", "secret_sauce")
    return InventoryPage(page)