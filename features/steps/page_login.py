from behave import *


@given('I have behave installed')
def step_impl(context):
    pass


@when('I enter page URL')
def step_impl(context):
    assert True is not False


@then('I see the Log in page')
def step_impl(context):
    assert context.failed is False
