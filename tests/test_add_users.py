import pytest
import json
import random
import string
from selenium import webdriver
from pages.user_table_page import UserTablePage
from utils.data_loader import load_users_from_csv
from utils.logger import get_logger
from selenium.webdriver.common.by import By

logger = get_logger()

# @pytest.fixture(scope="module")
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("http://www.way2automation.com/angularjs-protractor/webtables/")
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.mark.parametrize("user", load_users_from_csv("data/test_users.csv"))
def test_add_user(setup, user):
    page = UserTablePage(setup)
    page.validate_page()

    original_username = user["Username"]
    user["Username"] = generate_unique_username(original_username)

    logger.info(f"Adding user: {user['Username']}")
    page.add_user(user)
    body_text = setup.find_element(By.TAG_NAME, "body").text
    assert user["Username"] in body_text
    
def generate_unique_username(base_username):
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{base_username}_{suffix}"