from selenium.webdriver.common.by import By
from helpers.helpers import find_item_by_name
from pages.base_page import BasePage
from pages.regions.item import Item


class StorePage(BasePage):
    _products_list = (By.CSS_SELECTOR, "ul[class='products columns-4']")
    _product = (By.CSS_SELECTOR, "li[class*='product type-product']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._products_list)

    @property
    def items(self):
        return [Item(self, product) for product in self.find_elements(*self._product)]

    def add_item_to_cart(self, item_name):
        find_item_by_name(self.items, item_name).click_add_to_cart_button()
