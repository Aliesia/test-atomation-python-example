from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def invisibility_of_element_located(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def wait_for_page(self, expected_title, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.title_is(expected_title))
