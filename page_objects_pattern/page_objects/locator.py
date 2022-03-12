from selenium.webdriver.common.by import By

class Locators(object):
    """A class for main page locators."""
    PAGE_TITLE = (By.XPATH, "//h1[text()='My posts']")
    NEW_POST_TITLE = (By.ID, "title")
    NEW_POST_DESCRIPTION = (By.ID, "body")
    CARD_TITLES = (By.CSS_SELECTOR, ".Card--body-title")
    ADD_POST_BUTTON = (By.CLASS_NAME, "Form__button")
    DELETE_BUTTON = (By.CLASS_NAME, "Card__button")
