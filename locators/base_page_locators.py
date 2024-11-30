from selenium.webdriver.common.by import By


class BasePageLocators:
    zakaz_button = [By.XPATH, ".//button[text()='Заказать']"]# кнопка Заказать
    status_zakaza_button = [By.XPATH, ".//button[text()='Статус заказа']"]#кнопка Статус заказа