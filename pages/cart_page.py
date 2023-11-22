from selenium.webdriver.common.by import By
from helpers.helpers import find_item_in_cart_by_name
from pages.base_page import BasePage
from pages.regions.item_in_cart import ItemInCart
from pages.regions.menu_region import MenuRegion


class CartPage(BasePage):
    _cart_title = (By.XPATH, "//h1[contains(text(), 'Koszyk')]")
    _product_in_the_cart = (By.CSS_SELECTOR, "tr[class*='cart_item']")
    _delivery_fee = (By.CSS_SELECTOR, "td[data-title='Wysyłka'] span[class*='Price-amount']")
    _vat = (By.CSS_SELECTOR, "td[data-title='VAT'] span[class*='Price-amount']")
    _order_total_amount = (By.CSS_SELECTOR, "td[data-title='Łącznie'] span[class*='Price-amount']")
    _checkout_button = (By.XPATH, "//a[@class='checkout-button button alt wc-forward']")
    _successfully_removed_message = (By.CSS_SELECTOR, "div[class='woocommerce-message']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._cart_title)

    @property
    def items_in_the_cart(self):
        return [ItemInCart(self, product) for product in self.find_elements(*self._product_in_the_cart)]

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

        item = find_item_in_cart_by_name(self.items_in_the_cart, item_name)

        assert item.item_unit_price == item_unit_price
        assert item.quantity == quantity
        assert item.item_total_price == total_price

    def verify_removed_item_message(self, item_name):
        message = self.wait.until(self.ec.visibility_of_element_located(self._successfully_removed_message))
        assert message.text == f"Usunięto: „{item_name}”. Cofnij?"

    def click_checkout_button(self):
        self.find_element(*self._checkout_button).click()

    def remove_item_from_cart(self, item_name):
        menu = MenuRegion(self)
        amount_before_change = self.menu.amount
        find_item_in_cart_by_name(self.items_in_the_cart, item_name).click_remove_item_from_cart_button()

        self.wait.until(
            lambda page: amount_before_change != menu.amount,
            f"Amount is equal to {menu.amount} after adding item to cart!",
        )
