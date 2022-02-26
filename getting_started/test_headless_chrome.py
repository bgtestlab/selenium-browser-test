from selenium import webdriver


def test_run_headless_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--dns-prefetch-disable")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options,
    )

    driver.get(url="https://www.google.com/")
    driver.get_screenshot_as_file("google.png")
    driver.quit()
