from selenium.webdriver.common.by import By
from pages.regions.base_region import BaseRegion


class Item(BaseRegion):
    _name = (By.CSS_SELECTOR, "h2[class*='woocommerce-loop-product']")
    _add_to_cart_button = (By.CSS_SELECTOR, "a[class*='add_to_cart_button']")

    @property
    def name(self):
        return self.find_element(*self._name).text

    def click_add_to_cart_button(self):
        self.find_element(*self._add_to_cart_button).click()
