from selenium.webdriver.common.by import By
from pageobjects.guest_view.login_locators import LoginPageLocators


class ResetPasswordPageLocators(LoginPageLocators):
    BUTTON_BACK_TO_LOGIN = (By.CSS_SELECTOR, '.pV7Qt .yWX7d')

