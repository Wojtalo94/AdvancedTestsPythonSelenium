import pytest
from selenium import webdriver
from config.config import HEADLESS, FULLSCREEN


@pytest.fixture()
def driver(request):
    options = chrome_options()
    chrome_driver = webdriver.Chrome(options=options)
    request.cls.driver = chrome_driver
    yield chrome_driver
    chrome_driver.quit()


def chrome_options():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    if FULLSCREEN:
        options.add_argument("--start-fullscreen")

    return options
