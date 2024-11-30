import pytest
from selenium import webdriver

from pages.main_page import MainPage




@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


