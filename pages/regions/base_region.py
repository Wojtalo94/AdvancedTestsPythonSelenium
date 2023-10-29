from pypom import Region
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec


class BaseRegion(Region):
    def __init__(self, page, root=None):
        super().__init__(page, root)
        self.actions = ActionChains(page.driver)
        self.ec = ec
