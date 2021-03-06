from behave import *
from config.app import *
from pageobjects.guest_view.login_page import LoginPage


@given('I opened browser')
def step_impl(context):
    pass


@given('I enter page URL')
def step_impl(context):
    context.driver.get(INSTAGRAM_LOGIN_PAGE_URL)


@when('I enter page URL')
def step_impl(context):
    context.driver.get(INSTAGRAM_LOGIN_PAGE_URL)


@when('I click {button_name} button')
def step_impl(context, button_name):
    login_page = LoginPage(context.driver)
    login_page.click_button(button_name)


@when('I change language on {selected_language}')
def step_impl(context, selected_language):
    login_page = LoginPage(context.driver)
    switcher = {
        'Ukrainian': 'Українська'
    }

    login_page.set_selected_language(switcher.get(selected_language))


@when('I fill password field with {role} password')
def step_impl(context, role):
    login_page = LoginPage(context.driver)
    switcher = {
        'my': MY_PASSWORD,
        'wrong': WRONG_PASSWORD
    }
    login_page.field_password(switcher.get(role))


@when('I fill username field with {role} username')
def step_impl(context, role):
    login_page = LoginPage(context.driver)
    switcher = {
        'wrong': WRONG_LOGIN
    }
    login_page.field_username(switcher.get(role))


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
        'Google Play': GOOGLE_PLAY_URL
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


@then('I see the language changed on {selected_language}')
def step_impl(context, selected_language):
    login_page = LoginPage(context.driver)
    switcher = {
        'Ukrainian': 'Українська'
    }
    actual_language = login_page.get_selected_language()
    expected_language = switcher.get(selected_language)
    assert expected_language == actual_language


@then('I see the password is shown')
def step_impl(context):
    login_page = LoginPage(context.driver)
    actual_type = login_page.get_type_of_password()
    expected_type = 'text'
    assert expected_type == actual_type


@then('I see warning message on page')
def step_impl(context):
    login_page = LoginPage(context.driver)
    assert login_page.get_text_color() == 'rgba(237, 73, 86, 1)'
