import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators



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

    @allure.step('Клик на Лого Самокат')
    def click_to_logo_samokat(self):
        self.click_to_element(OrderPageLocators.LOGO_SAMOKAT)

    @allure.step('Клик на Лого Яндекс')
    def click_to_logo_yandex(self):
        self.click_to_element(OrderPageLocators.LOGO_YANDEX)

    @allure.step('Заполнение поля "Про Аренду"')
    def set_order2(self, date, color):
        self.add_date(OrderPageLocators.DATE_FIELD, date)
        self.click_to_element(color)
        self.click_to_element(OrderPageLocators.TIME_FIELD)
        self.click_to_element(OrderPageLocators.SUTOK4)
        self.click_to_element(OrderPageLocators.ZAKAZAT_BUTTON)
        self.click_to_element(OrderPageLocators.DA_BUTTON)

    @allure.step('Клик на "Заказать"')
    def click_to_zakaz(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Переключяемся на другое окно"')
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    @allure.step('Проверяем элемент на странице "Дзена"')
    def check_dzen(self):
        self.find_element_with_wait(OrderPageLocators.DZEN_LOC)












