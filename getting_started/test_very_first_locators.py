from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="module", autouse=True)
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # to keep browser open
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver


@pytest.fixture
def data_generator():
    def _data(title=None, desc=None):
        title = title or "My awesome book"
        desc = desc or "Fantastic!"
        return {
            "title": title,
            "description": desc,
        }

    return _data


def _write_post(driver, data_generator, test_title=None, test_desc=None):
    # Get test data
    post: dict = data_generator(test_title, test_desc)
    post_title = post["title"]
    post_description = post["description"]

    # Input 'Title'
    title = driver.find_element(By.ID, "title")
    title.clear()
    title.send_keys(post_title)

    # Input 'Description'
    description_locator = locate_with(By.TAG_NAME, "input").below({By.ID: "title"})
    description = driver.find_element(description_locator)
    description.clear()
    description.send_keys(post_description)

    # Click 'Add Post'
    button = driver.find_element(By.CLASS_NAME, "Form__button")
    button.click()

    sleep(2)


def test_open_test_page(driver):
    """Precondition: clone and run a test app from https://github.com/ibrahima92/next-typescript-example"""
    driver.get("http://localhost:3000/")

    # Check if landed
    driver.find_element(By.XPATH, "//h1[text()='My posts']")


def test_write_first_post(driver, data_generator):
    _write_post(driver, data_generator)


def test_check_if_post_is_present(driver, data_generator):
    # Get test data
    post: dict = data_generator()
    post_title = post["title"]
    post_description = post["description"]
    title_value = f"//h1[@class='Card--body-title' and text()='{post_title}']"
    description_value = f"//p[@class='Card--body-text' and text()='{post_description}']"

    # Set WebDriverWait
    wait = WebDriverWait(driver, 3, poll_frequency=1)

    # Try to get 'Title'
    wait.until(EC.visibility_of_element_located((By.XPATH, title_value)))

    # Try to get 'Description'
    wait.until(EC.visibility_of_element_located((By.XPATH, description_value)))

    sleep(2)


def test_delete_post(driver, data_generator):
    # Get test data
    post: dict = data_generator()
    post_title = post["title"]
    title_value = f"//h1[@class='Card--body-title' and text()='{post_title}']"

    # Set WebDriverWait
    wait = WebDriverWait(driver, 3, poll_frequency=1)

    # Delete post
    delete_locator = locate_with(By.CLASS_NAME, "Card__button").to_right_of(
        {By.XPATH: title_value}
    )
    delete = driver.find_element(delete_locator)
    delete.click()

    # Check if deleted
    wait.until(EC.invisibility_of_element_located((By.XPATH, title_value)))

    sleep(2)


def test_write_another_post(driver, data_generator):
    _write_post(driver, data_generator, "My second post", "also awesome!")

    sleep(2)


def test_get_all_the_post_titles(driver):
    titles = driver.find_elements(By.CSS_SELECTOR, ".Card--body-title")
    titles_list = [e.text for e in titles]

    for index, value in enumerate(titles_list):
        print(f"{index + 1}: {value}")
