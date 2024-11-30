import allure
import pytest
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from data import Data
from conftest import driver



class TestOrderPage:

    @allure.title('Тестирование формы заполнения')
    @allure.description('На странице нпроверяем обе кнопки заказа, а так же что заказ оформлен с разными наборами данных')
    @pytest.mark.parametrize(
        'locator, name, ser_name, address, tel, metro, loc_metro, date, color',
        [
            (OrderPageLocators.ORDER_BUTTON, Data.NAME, Data.SER_NAME, Data.ADDRESS, Data.TEL, Data.METRO, OrderPageLocators.SOKOL_METRO, Data.DATE, OrderPageLocators.BLACK_BUTTON),
            (OrderPageLocators.ORDER_BUTTON_MID, Data.NAME1, Data.SER_NAME1, Data.ADDRESS1, Data.TEL1, Data.METRO1, OrderPageLocators.KOLOM_METRO, Data.DATE1, OrderPageLocators.GREY_BUTTON)
        ]
    )
    def test_create_order(self, driver, locator, name, ser_name, address, tel, metro, loc_metro, date, color):
        order_page = OrderPage(driver)
        order_page.get_url(Data.URL)
        order_page.click_to_order(locator)
        order_page.set_order(name, ser_name, address, tel, metro, loc_metro)
        order_page.set_order2(date, color)
        assert "Заказ оформлен" in order_page.check_order()

    @allure.title('Тестирование клика на Лого Самоката')
    @allure.description('Проверяем переход на страницу по клику на Логотип')
    def test_logo_samokat(self, driver):
        order_page = OrderPage(driver)
        order_page.get_url(Data.URL)
        order_page.click_to_zakaz()
        order_page.click_to_logo_samokat()
        assert order_page.check_url() == Data.URL_SAMOKAT


    @allure.title('Тестирование клика на Лого Яндекса')
    @allure.description('Проверяем переход на страницу по клику на Логотип и находим элемент на ней')
    def test_logo_yandex(self, driver):
        order_page = OrderPage(driver)
        order_page.get_url(Data.URL)
        order_page.click_to_logo_yandex()
        order_page.switch_window()
        order_page.check_dzen()