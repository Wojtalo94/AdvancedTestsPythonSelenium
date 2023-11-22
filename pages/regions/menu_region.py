import time
from selenium.webdriver.common.by import By
from pages.regions.base_region import BaseRegion


class MenuRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "div[class='storefront-primary-navigation']")
    _store_button = (By.XPATH, ".//li[@id='menu-item-102']//a[contains(text(), 'Sklep')]")
    _my_account_button = (By.XPATH, ".//li[@id='menu-item-100']//a[contains(text(), 'Moje konto')]")
    _amount_to_pay = (By.CSS_SELECTOR, "a[class='cart-contents'] span[class*='Price-amount amount']")
    _cart_button = (By.XPATH, ".//li[@id='menu-item-99']//a[contains(text(), 'Koszyk')]")

    @property
    def amount(self):
        value = self.find_element(*self._amount_to_pay).text
        return value[1:]

    def open_store_page(self):
        self.find_element(*self._store_button).click()
        return self

    def open_my_account_page(self):
        self.find_element(*self._my_account_button).click()
        return self

    def open_cart_page(self):
        cart_button_element = self.wait.until(self.ec.element_to_be_clickable(self._cart_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_button_element)
        time.sleep(1)  # unfortunately, no other waiting for the page to scroll works so this sleep was used
        cart_button_element.click()
        return self

    def menu_pop_up(self):
        amount_element = self.find_element(*self._amount_to_pay)
        self.actions.move_to_element(amount_element).perform()
        return CartPopUpRegion(self)


class CartPopUpRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "div[class*='widget_shopping_cart_content']")
    _view_cart_button = (By.XPATH, ".//a[contains(text(), 'Zobacz koszyk')]")

    def go_to_the_cart(self):
        self.wait.until(self.ec.visibility_of_element_located(self._view_cart_button)).click()
        return self
