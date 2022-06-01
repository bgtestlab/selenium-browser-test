from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By

scenarios("search_engines.feature")


@given("I can see the google homepage")
def go_to_google(driver):
    driver.get(url="https://www.google.com/")
    driver.implicitly_wait(3)


@when("I enter the keyword 'hello' in the search box")
def search(driver):
    driver.find_element(By.TAG_NAME, "input").click()


@then("I should not see the error message")
def no_error_message(driver):
    pass


@given(parsers.parse("I can see the search engine {website} homepage"))
def go_to_search_engine(driver, website):
    driver.get(url=f"https://www.{website}")
    driver.implicitly_wait(3)
