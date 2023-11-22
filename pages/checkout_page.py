from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    _form = (By.CSS_SELECTOR, "form[name='checkout']")
    _first_name = (By.CSS_SELECTOR, "input[name='billing_first_name']")
    _last_name = (By.CSS_SELECTOR, "input[name='billing_last_name']")
    _address = (By.CSS_SELECTOR, "input[name='billing_address_1']")
    _postal_code = (By.CSS_SELECTOR, "input[name='billing_postcode']")
    _city = (By.CSS_SELECTOR, "input[name='billing_city']")
    _phone_number = (By.CSS_SELECTOR, "input[name='billing_phone']")
    _mail = (By.CSS_SELECTOR, "input[name='billing_email']")
    _buy_and_pay_button = (By.CSS_SELECTOR, "button[id='place_order']")
    _payment_blocker = (By.CSS_SELECTOR, "div[id='payment'] div[class='blockUI blockOverlay']")
    _success_message = (By.CSS_SELECTOR, "p[class*='thankyou-order-received']")
    _required_email_message = (By.CSS_SELECTOR, "li[data-id='billing_email']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._form)

    def fill_first_name(self, first_name):
        self.find_element(*self._first_name).send_keys(first_name)
        return self

    def fill_last_name(self, last_name):
        self.find_element(*self._last_name).send_keys(last_name)
        return self

    def fill_address(self, address):
        self.find_element(*self._address).send_keys(address)
        return self

    def fill_postal_code(self, postal_code):
        self.find_element(*self._postal_code).send_keys(postal_code)
        return self

    def fill_city(self, city):
        self.find_element(*self._city).send_keys(city)
        return self

    def fill_phone_number(self, phone_number):
        self.find_element(*self._phone_number).send_keys(phone_number)
        return self

    def fill_mail(self, mail):
        self.find_element(*self._mail).send_keys(mail)
        return self

    def clear_mail(self):
        self.find_element(*self._mail).clear()
        return self

    def buy_and_pay(self):
        self.wait.until(self.ec.invisibility_of_element_located(self._payment_blocker))
        self.wait.until(self.ec.element_to_be_clickable(self._buy_and_pay_button)).click()

    def verify_success_message(self):
        message = self.wait.until(self.ec.visibility_of_element_located(self._success_message))
        assert message.text == "Dziękujemy. Otrzymaliśmy Twoje zamówienie."

    def verify_the_required_email_message(self):
        message = self.wait.until(self.ec.visibility_of_element_located(self._required_email_message))
        assert message.text == "Adres e-mail płatnika jest wymaganym polem."
