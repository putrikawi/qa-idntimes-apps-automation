from behave import given, when, then
from py.pages.login_page import login


login_instance = login()

# start the driver
login_instance.start_driver()


@given("I have opened the app")
def step_impl(context):
    # Nothing to do here as the app is already opened
    pass


@when("I login with Google")
def step_impl(context):
    login_instance.login_with_google()


@when("I login with Facebook")
def step_impl(context):
    login_instance.login_with_facebook()


@when("I login with Email")
def step_impl(context):
    login_instance.login_with_email()


@then("I should be logged in successfully")
def step_impl(context):
    # Add your assertions here to check if the login was successful
    pass

#testpush

