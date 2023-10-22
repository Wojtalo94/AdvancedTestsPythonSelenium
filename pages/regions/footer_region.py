from selenium.webdriver.common.by import By
from pages.regions.base_region import BaseRegion


class FooterRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "p[class='woocommerce-store-notice demo_store']")
    _dismiss_button = (By.CSS_SELECTOR, "a[class*='_dismiss-link']")

    def click_dismiss_button(self):
        self.find_element(*self._dismiss_button).click()
