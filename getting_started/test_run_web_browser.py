from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_run_chrome_browser():
    service = Service(ChromeDriverManager().install())
    service.start()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # to keep browser open
    driver = webdriver.Remote(service.service_url, options=options)
    driver.get(url="https://www.google.com/")
