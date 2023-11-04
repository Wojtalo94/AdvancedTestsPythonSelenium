import os
from datetime import datetime

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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.failed:
        # Get the WebDriver instance from the test item
        driver = item.funcargs['driver']

        # Create a directory to save the screenshots
        screenshot_dir = 'screenshots'
        os.makedirs(screenshot_dir, exist_ok=True)

        # Generate a unique filename based on the test name and timestamp
        test_name = item.nodeid.replace('/', '_').replace(':', '-')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'{test_name}_{timestamp}.png'

        # Capture the screenshot and save it
        screenshot_path = os.path.join(screenshot_dir, filename)
        driver.save_screenshot(screenshot_path)

        # Add the screenshot path to the test report
        extra.append(pytest_html.extras.image(screenshot_path))
    report.extra = extra


def chrome_options():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    if FULLSCREEN:
        options.add_argument("--start-fullscreen")

    return options
