from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_browser_chrome(context):
    context.driver = webdriver.Chrome()
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
