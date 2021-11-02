from behave import * 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.environment import *
from features.pageobject.homepage import *
from features.scr.helper_function import *
use_step_matcher("re")

@when(u'type (.*) in (.*) field')
def step_impl(context, search_text, locator):
    search_bar_xpath = get_xpath_from_page(context, locator)
    input_field = context.driver.find_element_by_xpath(search_bar_xpath)
    input_field.clear()
    input_field.send_keys(search_text)

@when(u'click on (.*)')
def step_impl(context, locator):
    search_bar_xpath = get_xpath_from_page(context, locator)
    search_button = context.driver.find_element_by_xpath(search_bar_xpath)
    search_button.click()

@then(u'The result page url should have (.*) word')
def step_impl(context, search_word):
    assert search_word in context.driver.current_url 
# 1. make sure to check repeated code, but it in the fun.
# 2. change step function name  