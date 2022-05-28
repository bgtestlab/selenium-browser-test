def test_run_headless_chrome(driver):
    driver.get(url="https://www.google.com/")
    driver.get_screenshot_as_file("google.png")
