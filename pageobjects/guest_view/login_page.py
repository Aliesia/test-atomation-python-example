from pageobjects.base_page import *
from pageobjects.guest_view.login_locators import LoginPageLocators


class LoginPage(BasePage):
    def click_button(self, button_name):
        if button_name == 'accept All Cookie Policy':
            self.wait_for_element(LoginPageLocators.BUTTON_ACCEPT_ALL_COOKIES).click()

    def get_modal_window_title(self):
        return self.wait_for_element(LoginPageLocators.TITLE_MODAL_WINDOW).text
