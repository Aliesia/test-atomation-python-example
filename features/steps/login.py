from behave import *
from pageobjects.guest_view.login_page import LoginPage


@given('I opened browser')
def step_impl(context):
    pass


@given('I enter page URL')
def step_impl(context):
    context.driver.get('https://www.instagram.com/')


@when('I enter page URL')
def step_impl(context):
    context.driver.get('https://www.instagram.com/')


@when('I click {button_name} button')
def step_impl(context, button_name):
    login_page = LoginPage(context.driver)
    login_page.click_button(button_name)


@then('I see the Login page')
def step_impl(context):
    assert "Instagram" in context.driver.title


@then('I see Cookie Policy pop-up')
def step_impl(context):
    login_page = LoginPage(context.driver)
    expected_title = 'Accept cookies from Instagram on this browser?'
    assert login_page.get_modal_window_title() == expected_title
