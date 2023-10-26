from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    _cart_title = (By.XPATH, "//h1[contains(text(), 'Koszyk')]")
    _product_in_the_cart = (By.CSS_SELECTOR, "tr[class*='cart_item']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._cart_title)

    @property
    def items_in_the_cart(self):
        return [CartItem(self, product) for product in self.find_elements(*self._product_in_the_cart)]


class CartItem(BasePage):
    _name = (By.CSS_SELECTOR, "td[class*='product-name']")
    _item_unit_price = (By.CSS_SELECTOR, "td[class*='product-price']")
    _quantity = (By.CSS_SELECTOR, "td[class*='product-quantity'] input[aria-label='Ilość produktu']")
    _item_total_price = (By.CSS_SELECTOR, "td[class*='product-subtotal'] ")

    @property
    def name(self):
        return self.find_element(*self._name).text

    @property
    def item_unit_price(self):
        price = self.find_element(*self._item_unit_price).text
        return price[1:]

    @property
    def quantity(self):
        item_quantity = self.find_element(*self._name).text
        return item_quantity.get_atribute("value")

    @property
    def item_total_price(self):
        price = self.find_element(*self._item_total_price).text
        return price[1:]
