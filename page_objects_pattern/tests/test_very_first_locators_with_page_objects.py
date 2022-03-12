import logging
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects_pattern.page_objects.locator import Locators


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


class TestMyPostsPage:
    def _write_post(self, page, data_generator, test_title=None, test_desc=None):
        # Get test data
        post: dict = data_generator(test_title, test_desc)
        post_title = post["title"]
        post_description = post["description"]

        # Input 'Title'
        title = page.element(Locators.NEW_POST_TITLE).find()
        title.clear()
        title.send_keys(post_title)

        # Input 'Description'
        description = page.element(Locators.NEW_POST_DESCRIPTION).find()
        description.clear()
        description.send_keys(post_description)

        # Click 'Add Post'
        button = page.element(Locators.ADD_POST_BUTTON).find()
        button.click()

        sleep(2)

    def test_open_test_page(self, page):
        """Prerequisites: clone and run a test app from https://github.com/ibrahima92/next-typescript-example"""
        page.driver.get("http://localhost:3000/")

        # Check if landed
        page.element(Locators.PAGE_TITLE).find()

    def test_write_first_post(self, page, data_generator):
        self._write_post(page, data_generator)

    def test_check_if_post_is_present(self, page, data_generator):
        # Get test data
        post: dict = data_generator()
        post_title = post["title"]
        post_description = post["description"]
        title_value = f"//h1[@class='Card--body-title' and text()='{post_title}']"
        description_value = f"//p[@class='Card--body-text' and text()='{post_description}']"

        # Set WebDriverWait
        wait = WebDriverWait(page.driver, 3, poll_frequency=1)

        # Try to get 'Title'
        wait.until(EC.visibility_of_element_located((By.XPATH, title_value)))

        # Try to get 'Description'
        wait.until(EC.visibility_of_element_located((By.XPATH, description_value)))

        sleep(2)

    def test_delete_post(self, page, data_generator):
        # Get test data
        post: dict = data_generator()
        post_title = post["title"]
        title_value = f"//h1[@class='Card--body-title' and text()='{post_title}']"

        # Set WebDriverWait
        wait = WebDriverWait(page.driver, 3, poll_frequency=1)

        # Delete post
        delete_by, delete_using = Locators.DELETE_BUTTON
        delete_locator = locate_with(delete_by, delete_using).to_right_of(
            {By.XPATH: title_value}
        )
        delete = page.driver.find_element(delete_locator)
        delete.click()

        # Check if deleted
        wait.until(EC.invisibility_of_element_located((By.XPATH, title_value)))

        sleep(2)

    def test_write_another_post(self, page, data_generator):
        self._write_post(page, data_generator, "My second post", "also awesome!")

        sleep(2)

    def test_get_all_the_post_titles(self, page):
        titles_by, titles_using = Locators.CARD_TITLES
        titles = page.driver.find_elements(titles_by, titles_using)
        titles_list = [e.text for e in titles]

        for index, value in enumerate(titles_list):
            logging.info(f"{index + 1}: {value}")
