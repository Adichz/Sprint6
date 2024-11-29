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

    @allure.title('Тестирование кликов на Логотипы')
    @allure.description('Проверяем переходы на страницы по клику на Логотипы')
    @pytest.mark.parametrize(
        'locator, locator_logo, logo_url',
        [
            (OrderPageLocators.ORDER_BUTTON, OrderPageLocators.LOGO_SAMOKAT, Data.URL_SAMOKAT),
            (OrderPageLocators.ORDER_BUTTON_MID, OrderPageLocators.LOGO_YANDEX, Data.URL_YANDEX)
        ]
    )
    def test_logo(self, driver, locator, locator_logo, logo_url):
        order_page = OrderPage(driver)
        order_page.get_url(Data.URL)
        order_page.click_to_order(locator)
        order_page.click_to_logo(locator_logo)
        assert order_page.check_url() == logo_url




