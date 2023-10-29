from selenium.webdriver.common.by import By
from helpers.helpers import find_item_by_name
from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion


class CartPage(BasePage):
    _cart_title = (By.XPATH, "//h1[contains(text(), 'Koszyk')]")
    _product_in_the_cart = (By.CSS_SELECTOR, "tr[class*='cart_item']")
    _delivery_fee = (By.CSS_SELECTOR, "td[data-title='Wysyłka'] span[class*='Price-amount']")
    _vat = (By.CSS_SELECTOR, "td[data-title='VAT'] span[class*='Price-amount']")
    _order_total_amount = (By.CSS_SELECTOR, "td[data-title='Łącznie'] span[class*='Price-amount']")
    _checkout_button = (By.XPATH, "//a[@class='checkout-button button alt wc-forward']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._cart_title)

    @property
    def items_in_the_cart(self):
        return [CartItem(self, product) for product in self.find_elements(*self._product_in_the_cart)]

    @property
    def delivery_fee(self):
        fee = self.find_element(*self._delivery_fee).text
        return fee[1:]

    @property
    def vat(self):
        vat_fee = self.find_element(*self._vat).text
        return vat_fee[1:]

    @property
    def order_total_amount(self):
        total_amount = self.find_element(*self._order_total_amount).text
        return total_amount[1:]

    def assert_item_data(self, item_name, item_unit_price, quantity="1", total_price=None):
        if total_price is None:
            total_price = item_unit_price

        item = find_item_by_name(self.items_in_the_cart, item_name)

        assert item.item_unit_price == item_unit_price
        assert item.quantity == quantity
        assert item.item_total_price == total_price

    def click_checkout_button(self):
        self.find_element(*self._checkout_button).click()


class CartItem(BaseRegion):
    _name = (By.CSS_SELECTOR, "td[class*='product-name']")
    _item_unit_price = (By.CSS_SELECTOR, "td[class*='product-price']")
    _quantity = (By.CSS_SELECTOR, "td[class*='product-quantity'] input[id*='quantity']")
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
        item_quantity = self.find_element(*self._quantity)
        return item_quantity.get_attribute("value")

    @property
    def item_total_price(self):
        price = self.find_element(*self._item_total_price).text
        return price[1:]
