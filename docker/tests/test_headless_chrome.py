def test_if_succeeded(driver):
    driver.get(url="https://www.google.com/")


def test_if_failed(driver):
    driver.get(url="https://www.naver.com/")
    assert False


