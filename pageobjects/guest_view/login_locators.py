from selenium.webdriver.common.by import By
from pageobjects.base_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):
    BUTTON_ACCEPT_ALL_COOKIES = (By.CSS_SELECTOR, '.bIiDR')
    TITLE_MODAL_WINDOW = (By.CSS_SELECTOR, 'h2')
