import os
import sys
import time
from datetime import datetime

import pytest
from selenium import webdriver
from collections import OrderedDict

test_results = OrderedDict()


def get_current_test():
    """Just a helper function to extract the current test"""
    full_name = os.environ.get("PYTEST_CURRENT_TEST").split(" ")[0]
    test_file = full_name.split("::")[0].split("/")[-1].split(".py")[0]
    test_name = full_name.split("::")[1]
    return full_name, test_file, test_name


def _take_screenshot(driver, nodeid):
    time.sleep(1)
    path = f"{os.getcwd()}/screenshots/"
    if not (os.path.isdir(path)):
        os.makedirs(os.path.join(path))

    file_name = (
        f"{datetime.today().strftime('%Y-%m-%d_%H:%M')}_{nodeid.split('::')[1]}.png"
    )

    driver.save_screenshot(f"{path}{file_name}")
    screenshot = driver.get_screenshot_as_base64()
    return screenshot


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # Setup report file
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            driver = item.funcargs["driver"]
            screenshot = _take_screenshot(driver, nodeid=report.nodeid)
            extra.append(pytest_html.extras.image(screenshot, ""))
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra


@pytest.fixture(scope="session", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(
        command_executor="http://selenium-hub:4444",
        options=options,
    )
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()
