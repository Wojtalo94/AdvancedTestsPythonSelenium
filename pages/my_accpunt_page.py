from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyAccountPage(BasePage):
    _user_login_and_registration = (By.CSS_SELECTOR, "div[id='customer_login']")
    _email_or_login = (By.CSS_SELECTOR, "input[id='username']")
    _password = (By.CSS_SELECTOR, "input[id='password']")
    _login_button = (By.CSS_SELECTOR, "button[name='login']")
    _logout_button = (By.CSS_SELECTOR, "li[class*='customer-logout']")
    _logged_in_as_message = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']//p[contains(text(),'Witaj')]")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._user_login_and_registration)

    def fill_email_or_login(self, email_or_login):
        self.find_element(*self._email_or_login).send_keys(email_or_login)
        return self

    def fill_password(self, password):
        self.find_element(*self._password).send_keys(password)
        return self

    def login(self):
        self.find_element(*self._login_button).click()

    def logout(self):
        self.find_element(*self._logout_button).click()
        self.wait.until(self.ec.visibility_of_element_located(self._user_login_and_registration))

    def logged_in_as(self, username):
        logged_in_user = self.wait.until(self.ec.visibility_of_element_located(self._logged_in_as_message))
        assert logged_in_user.text == f"Witaj {username} (nie jesteś {username}? Wyloguj się)"
