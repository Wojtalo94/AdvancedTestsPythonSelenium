from pypom import Page
from config import config
from selenium.webdriver.support.wait import WebDriverWait
from pages.regions.menu_region import MenuRegion
from pages.regions.footer_region import FooterRegion
from selenium.webdriver.support import expected_conditions as ec


class BasePage(Page):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)
        self.base_url = config.BASE_URL
        self.wait = WebDriverWait(driver, config.MAX_WAIT)
        self.ec = ec

    @property
    def menu(self):
        return MenuRegion(self)

    @property
    def footer(self):
        return FooterRegion(self)
