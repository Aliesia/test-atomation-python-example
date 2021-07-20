from selenium.webdriver.common.by import By
from pageobjects.base_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):
    BUTTON_ACCEPT_ALL_COOKIES = (By.CLASS_NAME, 'bIiDR')
    BUTTON_GET_APP_WITH_GOOGLE = (By.CSS_SELECTOR, '.z1VUo+ .z1VUo .Rt8TI')
    BUTTON_FORGOT_PASSWORD = (By.CLASS_NAME, '_2Lks6')
    BUTTON_SIGN_UP = (By.CLASS_NAME, 'se6yk')
    BUTTON_LOG_IN_WITH_FACEBOOK = (By.CLASS_NAME, 'KPnG0')
    BUTTON_TOP_ACCOUNTS = (By.CSS_SELECTOR, '.JI_ht:nth-child(8) .uL8Hv')
    TITLE_MODAL_WINDOW = (By.CSS_SELECTOR, 'h2')
    LINK_URL = (By.CSS_SELECTOR, '.z1VUo:nth-of-type(2)')
