import allure
import pytest
from selenium import webdriver
from conftest import driver
from pages.main_page import MainPage
from data import Data



@allure.title('Тест вопросов и ответов')
@allure.description('На странице скроллим вниз и проверяем ответы на вопросы по списку')
class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, Data.A0),
            (1, Data.A1),
            (2, Data.A2),
            (3, Data.A3),
            (4, Data.A4),
            (5, Data.A5),
            (6, Data.A6),
            (7, Data.A7)
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.get_url(Data.URL)
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == result



