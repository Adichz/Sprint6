import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderPage(BasePage):

    @allure.step('Выбор станции метро')
    def set_metro(self, metro, loc_metro):
        self.add_text_to_element(OrderPageLocators.METRO_STATION, metro)
        self.click_to_element(loc_metro)

    @allure.step('Заполнение поля "Для кого самокат"')
    def set_order(self, name, ser_name, address,tel,  metro, loc_metro):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)
        self.add_text_to_element(OrderPageLocators.SERNAME_FIELD, ser_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS, address)
        self.add_text_to_element(OrderPageLocators.TELEPHON, tel)
        self.set_metro(metro, loc_metro)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Проверка заказа')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.FINAL_FIELD)

    @allure.step('Клик на Лого')
    def click_to_logo(self, locator_logo):
        self.click_to_element(locator_logo)

    @allure.step('Заполнение поля "Про Аренду"')
    def set_order2(self, date, color):
        self.add_date(OrderPageLocators.DATE_FIELD, date)
        self.click_to_element(color)
        self.click_to_element(OrderPageLocators.TIME_FIELD)
        self.click_to_element(OrderPageLocators.SUTOK4)
        self.click_to_element(OrderPageLocators.ZAKAZAT_BUTTON)
        self.click_to_element(OrderPageLocators.DA_BUTTON)










