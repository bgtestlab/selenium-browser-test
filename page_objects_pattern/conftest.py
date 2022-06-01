import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from page_objects_pattern.page_objects.page import Page


@pytest.fixture(scope="package", autouse=True)
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # to keep browser open
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver


@pytest.fixture(scope="package", autouse=True)
def page(driver):
    page = Page(driver)
    yield page
