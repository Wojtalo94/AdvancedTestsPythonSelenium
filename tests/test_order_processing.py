import pytest
from config import config
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.store_page import StorePage
from pages.my_accpunt_page import MyAccountPage


@pytest.mark.usefixtures("driver")
@pytest.mark.flaky(reruns=config.RERUN)
class TestOrderProcessing:
    def test_order_product_as_a_gest(self):
        home_page = HomePage(self.driver).open()
        home_page.footer.click_dismiss_button()
        home_page.menu.open_store_page()

        store_page = StorePage(self.driver).wait_for_page_to_load()
        store_page.add_item_to_cart("Belt")

        assert home_page.menu.amount == "65,00"
        home_page.menu.menu_pop_up().go_to_the_cart()

        cart_page = CartPage(self.driver).wait_for_page_to_load()
        cart_page.assert_item_data("Belt", "65,00")

        assert cart_page.delivery_fee == "5,00"
        assert cart_page.vat == "16,10"
        assert cart_page.order_total_amount == "86,10"

        cart_page.click_checkout_button()

        checkout_page = CheckoutPage(self.driver).wait_for_page_to_load()
        checkout_page.fill_first_name("John").fill_last_name("Doe")
        checkout_page.fill_address("Test Street 33").fill_postal_code("33-333").fill_city("London")
        checkout_page.fill_phone_number("123456789").fill_mail("john@test.com")
        checkout_page.buy_and_pay()
        checkout_page.verify_success_message()

    def test_validation_of_an_email_field_when_ordering_as_a_user(self):
        home_page = HomePage(self.driver).open()
        home_page.footer.click_dismiss_button()

        home_page.menu.open_my_account_page()
        my_account_page = MyAccountPage(self.driver).wait_for_page_to_load()
        my_account_page.fill_email_or_login("cotaga1249@maillei.net").fill_password("VRrMhK8MqFyd")
        my_account_page.login()
        my_account_page.logged_in_as("cotaga1249")

        home_page.menu.open_store_page()
        store_page = StorePage(self.driver).wait_for_page_to_load()
        store_page.add_item_to_cart("Belt")
        assert home_page.menu.amount == "65,00"
        store_page.add_item_to_cart("Cap")
        assert home_page.menu.amount == "83,00"

        home_page.menu.menu_pop_up().go_to_the_cart()

        cart_page = CartPage(self.driver).wait_for_page_to_load()
        cart_page.assert_item_data("Belt", "65,00")
        cart_page.assert_item_data("Cap", "18,00")

        assert cart_page.delivery_fee == "5,00"
        assert cart_page.vat == "20,24"
        assert cart_page.order_total_amount == "108,24"

        cart_page.remove_item_from_cart("Belt")

        assert cart_page.delivery_fee == "5,00"
        assert cart_page.vat == "5,29"
        assert cart_page.order_total_amount == "28,29"
        cart_page.verify_removed_item_message("Belt")

        cart_page.click_checkout_button()

        checkout_page = CheckoutPage(self.driver).wait_for_page_to_load()
        checkout_page.clear_mail()

        checkout_page.buy_and_pay()

        checkout_page.verify_the_required_email_message()

        # data cleaning after the test is finished
        home_page.menu.open_cart_page()
        cart_page.remove_item_from_cart("Cap")
        assert home_page.menu.amount == "0,00"
        cart_page.verify_removed_item_message("Cap")
        home_page.menu.open_my_account_page()
        my_account_page.logout()
