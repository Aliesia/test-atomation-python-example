from selenium.webdriver.common.by import By
from pageobjects.base_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):
    TITLE_MODAL_WINDOW = (By.CSS_SELECTOR, 'h2')
