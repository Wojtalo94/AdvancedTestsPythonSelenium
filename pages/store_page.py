from selenium.webdriver.common.by import By
from helpers.helpers import find_item_in_store_by_name
from pages.base_page import BasePage
from pages.regions.item_in_store import ItemInStore
from pages.regions.menu_region import MenuRegion


class StorePage(BasePage):
    _products_list = (By.CSS_SELECTOR, "ul[class='products columns-4']")
    _product = (By.CSS_SELECTOR, "li[class*='product type-product']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._products_list)

    @property
    def items_in_store(self):
        return [ItemInStore(self, product) for product in self.find_elements(*self._product)]

    def add_item_to_cart(self, item_name):
        menu = MenuRegion(self)
        amount_before_change = self.menu.amount
        find_item_in_store_by_name(self.items_in_store, item_name).click_add_to_cart_button()
        self.wait.until(
            lambda page: amount_before_change != menu.amount,
            f"Amount is equal to {menu.amount} after adding item to cart!",
        )
