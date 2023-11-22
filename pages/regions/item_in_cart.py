from selenium.webdriver.common.by import By
from pages.regions.base_region import BaseRegion


class ItemInCart(BaseRegion):
    _name = (By.CSS_SELECTOR, "td[class*='product-name']")
    _item_unit_price = (By.CSS_SELECTOR, "td[class*='product-price']")
    _quantity = (By.CSS_SELECTOR, "td[class*='product-quantity'] input[id*='quantity']")
    _item_total_price = (By.CSS_SELECTOR, "td[class*='product-subtotal'] ")
    _product_in_cart = (By.CSS_SELECTOR, "tr[class*='cart_item']")
    _remove_item_from_cart_button = (By.CSS_SELECTOR, "a[class='remove']")

    @property
    def cart_item_name(self):
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

    def click_remove_item_from_cart_button(self):
        self.wait.until(self.ec.element_to_be_clickable(self._remove_item_from_cart_button)).click()
