import pytest
from selenium import webdriver


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
