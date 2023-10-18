from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StorePage(BasePage):
    _products_list = (By.CSS_SELECTOR, "ul[class='products columns-4']")
    _product = (By.CSS_SELECTOR, "li[class*='product type-product']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._products_list)
