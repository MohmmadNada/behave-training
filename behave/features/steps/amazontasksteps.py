from behave import * 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.environment import *
from features.pageobject.homepage import *
from features.scr.helper_functions import *
use_step_matcher("re")

@when('the user navigate to Amazon (.*)')
def navigate_to_page(context, page):
    context.page = get_page_module(page)
    visit_page(context, context.page.url)
    
@when('the user click on the (.*) category')
def click_on(context, locator):
    first_card = get_element_from_feature(context, locator)
    first_card.click()

@when("the user should be redirect to Amazon (.*)")
def test_redirect_url(context, page):
    context.page = get_page_module(page) 
    assert context.page.url in context.driver.current_url
    
@then('the (.*) should be appear')
def test_display_element(context, locator):
    left_bar = get_element_from_feature(context, locator)
    left_bar.is_displayed()

@then('the (.*) should have (.*)')
def test_child_element_in_parent_element(context, parent_element, child_element):
    department_section =  get_element_inside_element(context, parent_element, child_element)
    department_section.is_displayed()
