from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.base_locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
