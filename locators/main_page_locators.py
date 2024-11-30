from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, './/*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, './/*[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, './/*[@id="accordion__heading-7"]'
    ORDER_BUTTON = By.XPATH, ".//button[text()='Заказать']"
    ORDER_BUTTON_MID = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
