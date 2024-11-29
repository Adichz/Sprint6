import pytest
from selenium import webdriver

from pages.main_page import MainPage




@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


#@pytest.fixture
#def main_page(driver):
#    page = MainPage(driver)
#    page.get_url(url)
#    return page