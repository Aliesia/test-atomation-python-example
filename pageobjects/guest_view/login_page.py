from pageobjects.base_page import *
from pageobjects.guest_view.login_locators import LoginPageLocators


class LoginPage(BasePage):
    def get_modal_window_title(self):
        return self.wait_for_element(LoginPageLocators.TITLE_MODAL_WINDOW).text
