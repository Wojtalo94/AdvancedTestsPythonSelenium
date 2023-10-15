import pytest
from selenium import webdriver
from config.config import HEADLESS, FULLSCREEN
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    options = chrome_options()
    chrome_driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)
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
