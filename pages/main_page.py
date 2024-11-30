import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)



