from behave import given, when, then
from login.test.factories.user import UserFactory


@given(u'an anonymous user')
def setp_impl(context):
    from django.contrib.auth.models import User
    # Creates dummy user for tests (it's not authenticated)
    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    u.save()


@when(u'I sumbit a valid login page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/login/')

    # Checks for CSRF protection
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('submit').click()


@then(u'I am redirected to the login success page')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/login/success/')
    assert br.find_element_by_id('main_title').text == "Login success"


@when(u'I submit an invalid login page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/login/')

    # Checks for CSFR protection
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (invalid version)
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar-is-invalid')
    br.find_element_by_name('submit').click()


@then(u'I am redirected to the login fail page')
def step_impl(context):
    br = context.browser

    # Checks redirectino URL
    assert br.current_url.endswith('/login/fail/')
    assert br.find_element_by_id('main_title').text == "Login failure"
