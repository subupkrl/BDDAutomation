from behave import *
from selenium.webdriver import Chrome
from behave.api.pending_step import StepNotImplementedError


@given(u'User is on registration page')
def step_imp(context):
    context.driver = Chrome()
    context.driver.get("https://www.facebook.com/r.php")
    context.driver.maximize_window()
    
@when(u'User enters firstname')
def step_imp(context):
    context.driver.find_element('name',"firstname").send_keys('Hello')


@when(u'User enters lastname')
def step_imp(context):
    context.driver.find_element('name',"lastname").send_keys('Sharma')


@when(u'User enters month')
def step_imp(context):
    context.driver.find_element('name','birthday_month').send_keys('Feb')


@when(u'User enters date')
def step_imp(context):
    context.driver.find_element('name','birthday_day').send_keys('28')


@when(u'User enters year')
def step_imp(context):
    context.driver.find_element('name','birthday_year').send_keys('2002')


@when(u'User clicks gender')
def step_imp(context):
    context.driver.find_element('xpath',"//input[@value='2']").click()


@when(u'User enters email')
def step_imp(context):
    context.driver.find_element('xpath',"//input[@name='reg_email__']").send_keys('hello@gmail.com')


@when(u'User enters new password')
def step_imp(context):
    context.driver.find_element('xpath',"//input[@name='reg_passwd__']").send_keys('Ram@1234')


@when(u'User click on Sign Up')
def step_imp(context):
    context.driver.find_element('xpath',"//button[@type='submit']").click()
    
    
@then(u'User should be registered successfully')
def step_imp(context):
    print('Registered')
    

@when(u'User enters duplicate email')
def step_impl(context):
    raise StepNotImplementedError(u'When User enters email')


@then(u'User should get duplicate email message')
def step_impl(context):
    raise StepNotImplementedError(u'Then User should get duplicate email message')