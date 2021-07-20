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


@then('I see the {page_name} page')
def step_impl(context, page_name):
    login_page = LoginPage(context.driver)
    if page_name == 'Login':
        assert 'Instagram' in context.driver.title
    elif page_name == 'Forgot password':
        login_page.wait_until_title_is('Reset Password • Instagram')
        assert 'Reset Password' in context.driver.title
    elif page_name == 'Sign up':
        login_page.wait_until_title_is('Login • Instagram')
        assert 'Login' in context.driver.title
    elif page_name == 'Log in with Facebook':
        assert 'Facebook' in context.driver.title
    elif page_name == 'Top Accounts':
        login_page.wait_until_title_is('Profiles • Instagram')
        assert 'Profiles' in context.driver.title


@then('I see Cookie Policy pop-up')
def step_impl(context):
    login_page = LoginPage(context.driver)
    expected_title = 'Accept cookies from Instagram on this browser?'
    assert login_page.get_modal_window_title() == expected_title


@then('I see {integration_name} integration link')
def step_impl(context, integration_name):
    login_page = LoginPage(context.driver)
    switcher = {
        'Google Play': 'https://play.google.com/store/apps/details?id=com.instagram.android'
    }
    actual_link = login_page.get_google_play_link()
    expected = switcher.get(integration_name)
    assert expected in actual_link


@then('I see {integration_name} integration link is clickable')
def step_impl(context, integration_name):
    login_page = LoginPage(context.driver)
    if integration_name == 'Google Play':
        return login_page.google_play_clickable_link()
    else:
        raise Exception('Element is not clickable')
