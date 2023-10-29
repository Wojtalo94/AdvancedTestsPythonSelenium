from selenium.webdriver.common.by import By
from helpers.helpers import find_item_by_name
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

    def assert_item_data(self, item_name, item_unit_price, quantity="1", total_price=None):
        if total_price is None:
            total_price = item_unit_price

        item = find_item_by_name(self.items_in_the_cart, item_name)

        assert item.item_unit_price == item_unit_price
        assert item.quantity == quantity
        assert item.item_total_price == total_price


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
        item_quantity = self.find_element(*self._quantity).text
        return item_quantity.get_atribute("value")

    @property
    def item_total_price(self):
        price = self.find_element(*self._item_total_price).text
        return price[1:]
