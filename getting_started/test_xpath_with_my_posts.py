from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


FICTION_BEST_SELLERS = [
    {"title": "불편한 편의점", "description": "저자: 김호연, 출판사: 나무옆의자, 판매순위:7"},
    {"title": "아몬드", "description": "저자: 손원평, 출판사: 창비, 판매순위:4"},
    {"title": "달러구트 꿈 백화점", "description": "저자: 이미예, 출판사: 팩토리나인, 판매순위:1"},
    {"title": "완전한 행복", "description": "저자: 정유정, 출판사: 은행나무, 판매순위:5"},
    {"title": "달러구트 꿈 백화점 2", "description": "저자: 이미예, 출판사: 팩토리나인, 판매순위:2"},
    {"title": "파친코1", "description": "저자: 김호연, 출판사: 나무옆의자, 판매순위:8"},
    {"title": "미드나잇 라이브러리", "description": "저자: 매트 헤이그, 출판사: 인플루엔셜, 판매순위:3"},
    {"title": "시선으로부터", "description": "저자: 정세랑, 출판사: 문학동네, 판매순위:10"},
    {"title": "파친코2", "description": "저자: 김호연, 출판사: 나무옆의자, 판매순위:9"},
    {
        "title": "오늘 밤, 세계에서 이 사랑이 사라진다 해도",
        "description": "저자: 이치조 미사키, 출판사: 모모, 판매순위:6",
    },
]  # sourced from http://ch.yes24.com/Article/View/46497


@pytest.fixture(scope="module", autouse=True)
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # to keep browser open
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver


def _write_post(driver, post_data):
    # Get test data
    post: dict = post_data
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


def test_delete_all_posts(driver):
    button_class_value = "Card__button"
    # Get all the button elements
    buttons = driver.find_elements(By.CLASS_NAME, button_class_value)

    # Click all the buttons
    for button in buttons:
        button.click()

    # Set WebDriverWait
    wait = WebDriverWait(driver, 3, poll_frequency=1)

    # Check if all deleted
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, button_class_value)))

    sleep(2)


@pytest.mark.parametrize("post", FICTION_BEST_SELLERS)
def test_add_ten_readable_posts_in_korean(driver, post):
    # Write post
    _write_post(driver, post)

    # Set WebDriverWait
    wait = WebDriverWait(driver, 3, poll_frequency=1)

    # Check if added
    title = post["title"]
    description = post["description"]
    title_value = f"//h1[@class='Card--body-title' and text()='{title}']"
    description_value = f"//p[@class='Card--body-text' and text()='{description}']"

    # Try to get 'Title'
    wait.until(EC.visibility_of_element_located((By.XPATH, title_value)))

    # Try to get 'Description'
    wait.until(EC.visibility_of_element_located((By.XPATH, description_value)))


def test_get_publisher_book_titles(driver):
    # Target publisher: '나무옆의자'
    target = "나무옆의자"

    # Choose target titles
    target_description_value = (
        f"//p[@class='Card--body-text' and contains(text(), '{target}')]"
    )
    target_title_value = f"{target_description_value}/preceding-sibling::h1"
    target_titles = driver.find_elements(By.XPATH, target_title_value)

    # Print titles to console
    for title in target_titles:
        print(f"title: {title.text}")
