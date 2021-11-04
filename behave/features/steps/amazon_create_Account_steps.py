from behave import * 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.environment import *
from features.pageobject.homepage import *
from features.scr.helper_functions import *
use_step_matcher("re")

@given('should be stay in the (.*)')
def is_in_the_same_page(context, page_name):
    context.page = get_page_module(page_name)
    assert context.page.url_key_word in context.driver.current_url
    # we cant save the url when we navigate to here and then check it here.
    # or add keys word in the class like register

@given('(.*) should be appear')# email_alert 
def is_text_alert_appear(context, alert_name):
    element = get_element_from_feature(context, alert_name)
    element.is_displayed()

@when('the user leave (.*) field empty')
def enter_empty_in_field(context, field_name):
    input_field = get_element_from_feature(context, field_name)
    input_field.clear()
    input_field.send_keys("")

@when('clear inputs fields')
def clear_input_field(context):

    get_xpath_from_page(context, context.page.user_name)
    get_xpath_from_page(context, context.page.user_email)
    get_xpath_from_page(context, context.page.user_password)
    get_xpath_from_page(context, context.page.user_password_matcher)
    
    # user_email
    # user_password
    # user_password_matcher