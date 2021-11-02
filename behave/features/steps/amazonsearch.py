from behave import * 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.environment import *
from features.pageobject.homepage import *
from features.scr.helper_function import *
import time

use_step_matcher("re")

@when(u'the user navigate to amazon (.*)')
def step_impl(context, page):
    context.page = get_page_module(page) 
    context.driver.get(context.page.url)
    
@when(u'type (.*) in (.*)')
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

@then(u'The (.*) url should have (.*) text')
def step_impl(context, page, seatch_text):
    context.page = get_page_module(page)
    context.page.url = context.driver.current_url
    assert seatch_text in context.page.url 
