from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class OrderPageLocators:

    ORDER_BUTTON = By.XPATH, ".//button[text()='Заказать']"
    ORDER_BUTTON_MID = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    METRO_STATION = By.XPATH, ".//div[@class='Order_Form__17u6u']//div[4]//input"
    NAME_FIELD = By.XPATH, ".//div[@class='Order_Form__17u6u']//div[1]/input"
    SERNAME_FIELD = By.XPATH, ".//div[@class='Order_Form__17u6u']//div[2]/input"
    ADDRESS = By.XPATH, ".//div[@class='Order_Form__17u6u']//div[3]/input"
    TELEPHON = By.XPATH, ".//div[@class='Order_Form__17u6u']//div[5]/input"
    NEXT_BUTTON = By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button"
    SOKOL_METRO = By.XPATH, ".//*[text()='Сокольники']"
    KOLOM_METRO = By.XPATH, ".//*[text()='Комсомольская']"
    DATE_FIELD = By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input"
    BLACK_BUTTON = By.XPATH, ".//*[@id='black']"
    GREY_BUTTON = By.XPATH, ".//*[@id='grey']"
    TIME_FIELD = By.XPATH, ".//div[@class='Dropdown-control']"
    SUTOK4 = By.XPATH, ".//div[@class='Dropdown-menu']/div[4]"
    SUTOK3 = By.XPATH, ".//div[@class='Dropdown-menu']/div[3]"
    ZAKAZAT_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DA_BUTTON = By.XPATH, ".//button[text()='Да']"
    FINAL_FIELD = By.XPATH , ".//div[@class='Order_ModalHeader__3FDaJ']"
    LOGO_SAMOKAT = By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"
    LOGO_YANDEX = By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"
