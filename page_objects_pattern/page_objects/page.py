from typing import Any
from selenium.webdriver.chrome.webdriver import WebDriver
from page_objects_pattern.page_objects.element import Element


class Page(object):
    """Base class to initialize pages"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element(self, locator: Any) -> Element:
        return Element(self.driver, locator)
