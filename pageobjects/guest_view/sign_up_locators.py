from selenium.webdriver.common.by import By
from pageobjects.guest_view.login_locators import LoginPageLocators


class SignUpLocators(LoginPageLocators):
    BUTTON_LOG_IN = (By.CSS_SELECTOR, '.izU2O a')
