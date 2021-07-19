from pageobjects.base_page import *
from pageobjects.guest_view.login_locators import LoginPageLocators


class LoginPage(BasePage):
    def click_button(self, button_name):
        if button_name == 'accept All Cookie Policy':
            self.wait_for_element(LoginPageLocators.BUTTON_ACCEPT_ALL_COOKIES).click()
        elif button_name == 'Get the app on Google play':
            self.wait_for_element(LoginPageLocators.BUTTON_GET_APP_WITH_GOOGLE).click()

    def get_modal_window_title(self):
        return self.wait_for_element(LoginPageLocators.TITLE_MODAL_WINDOW).text

    def get_google_play_link(self):
        return self.wait_for_element(LoginPageLocators.LINK_URL).get_attribute('href')

    def google_play_clickable_link(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.LINK_URL)
