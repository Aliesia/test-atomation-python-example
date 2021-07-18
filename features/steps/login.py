from behave import *


@given('Behave installed')
def step_impl(context):
    pass


@when('I enter page URL')
def step_impl(context):
    context.driver.get('https://www.instagram.com/')


@then('I see the Login page')
def step_impl(context):
    assert "Instagram" in context.driver.title
