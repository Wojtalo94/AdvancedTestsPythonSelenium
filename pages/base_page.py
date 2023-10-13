from pypom import Page
from selenium.webdriver.support.wait import WebDriverWait
from config import config


class BasePage(Page):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)
        self.base_url = config.BASE_URL
        self.wait = WebDriverWait(driver, config.MAX_WAIT)
