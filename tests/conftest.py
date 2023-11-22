import os
from datetime import datetime

import pytest
from selenium import webdriver
from config.config import HEADLESS, FULLSCREEN, REMOTE_MODE
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Remote


@pytest.fixture()
def driver(request):
    driver = remote_chromedriver() if REMOTE_MODE else local_chromedriver()
    request.cls.driver = driver
    yield driver
    driver.quit()


def local_chromedriver():
    options = chrome_options()
    chrome_driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)
    return chrome_driver


def remote_chromedriver() -> Remote:
    wd_hub = "http://selenium__standalone-chrome:4444/wd/hub"
    options = chrome_options()
    chrome_driver = webdriver.Remote(command_executor=wd_hub, options=options)
    return chrome_driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.failed:
        # Get the WebDriver instance from the test item
        driver = item.funcargs["driver"]

        # Create a directory to save the screenshots
        screenshot_dir = "reports"
        os.makedirs(screenshot_dir, exist_ok=True)

        # Generate a unique filename based on the test name and timestamp
        test_name = item.nodeid.replace("/", "_").replace(":", "-")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"

        # Capture the screenshot and save it
        screenshot_path = os.path.join(screenshot_dir, filename)
        driver.save_screenshot(screenshot_path)

        # Create html file with the screenshot to add to the report
        html = (
            f'<div><img src="{filename}" style="width:300px;height:230px;"'
            f'onclick="window.open(this.src)" align="right"/></div>'
        )
        extra.append(pytest_html.extras.html(html))

    report.extra = extra


def chrome_options():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    if FULLSCREEN:
        options.add_argument("--start-fullscreen")

    return options
