from selenium.webdriver.common.by import By
from pages.regions.base_region import BaseRegion


class MenuRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "div[class='storefront-primary-navigation']")
    _store_button = (By.XPATH, ".//li[@id='menu-item-102']//a[contains(text(), 'Sklep')]")

    def open_store_page(self):
        self.find_element(*self._store_button).click()
        return self
