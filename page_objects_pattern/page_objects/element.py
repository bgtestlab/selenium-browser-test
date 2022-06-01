from typing import Any, Optional
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_WAIT_TIME = 60


class Element:
    """A class for an page element"""

    def __init__(self, driver: WebDriver, locator: Any):
        self.driver = driver
        self.locator = locator
        self.web_element: Optional[WebElement] = None

    def find(self, time: int = DEFAULT_WAIT_TIME) -> WebElement:
        """Check if an element is visible. Return it if found"""
        element = WebDriverWait(driver=self.driver, timeout=time).until(
            EC.visibility_of_element_located(locator=self.locator)
        )

        self.web_element = element
        return self.web_element

    def click(self, time: int = DEFAULT_WAIT_TIME) -> None:
        """Send a click event to an element"""
        element = WebDriverWait(driver=self.driver, timeout=time).until(
            EC.element_to_be_clickable(mark=self.locator)
        )
        element.click()

    def clear(self, time: int = DEFAULT_WAIT_TIME) -> None:
        """Clear input of an element"""
        element = WebDriverWait(driver=self.driver, timeout=time).until(
            EC.element_to_be_clickable(mark=self.locator)
        )
        element.clear()

    def send_keys(self, data: Any) -> None:
        """Send keys to an element"""
        self.find()
        self.web_element.send_keys(data)
