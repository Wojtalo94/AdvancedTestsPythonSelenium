import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("driver")
class TestOrderProcessing:
    def test_order_product_as_a_gest(self):
        home_page = HomePage(self.driver).open()
        home_page.menu.open_store_page()
