from pageobjects.base_page import *
from pageobjects.guest_view.login_locators import LoginPageLocators
from pageobjects.guest_view.reset_password_locators import ResetPasswordPageLocators


class LoginPage(BasePage):
    def click_button(self, button_name):
        if button_name == 'accept All Cookie Policy':
            self.wait_for_element(LoginPageLocators.BUTTON_ACCEPT_ALL_COOKIES).click()
            self.invisibility_of_element_located(LoginPageLocators.BUTTON_ACCEPT_ALL_COOKIES)
        elif button_name == 'Get the app on Google play':
            self.wait_for_element(LoginPageLocators.BUTTON_GET_APP_WITH_GOOGLE).click()
        elif button_name == 'Forgot password':
            self.wait_for_element(LoginPageLocators.BUTTON_FORGOT_PASSWORD).click()
        elif button_name == 'Sign up':
            self.wait_for_element(LoginPageLocators.BUTTON_SIGN_UP).click()
        elif button_name == 'Log in with Facebook':
            self.wait_for_element(LoginPageLocators.BUTTON_LOG_IN_WITH_FACEBOOK).click()
        elif button_name == 'Top Accounts':
            self.wait_for_element(LoginPageLocators.BUTTON_TOP_ACCOUNTS).click()
        elif button_name == 'change Language':
            self.wait_for_element(LoginPageLocators.BUTTON_CHANGE_LANGUAGE).click()
        elif button_name == 'Back To Login':
            self.wait_for_element(ResetPasswordPageLocators.BUTTON_BACK_TO_LOGIN).click()

    def get_modal_window_title(self):
        return self.wait_for_element(LoginPageLocators.TITLE_MODAL_WINDOW).text

    def get_google_play_link(self):
        return self.wait_for_element(LoginPageLocators.LINK_URL).get_attribute('href')

    def google_play_clickable_link(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.LINK_URL)

    def wait_until_title_is(self, expected_title):
        self.wait_for_page(expected_title)

    def set_selected_language(self, language):
        return self.driver.find_element_by_xpath(LoginPageLocators.language_xpath_element(language)).click()

    def get_selected_language(self):
        return self.wait_for_element(LoginPageLocators.TITLE_LANGUAGE).text
