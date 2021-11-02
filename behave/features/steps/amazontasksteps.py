from behave import * 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.environment import *
from features.pageobject.homepage import *
from features.scr.helper_function import *
use_step_matcher("re")

@when('the user navigate to Amazon (.*)')
def step_impl(context, page):
    context.page = get_page_module(page)    
    context.driver.get(context.page.url)
    
@when('the user click on the (.*) category')
def step_impl(context, element):
    element = get_locoter_from_feature(element)
    element_xpath = get_xpath_from_page(context, element)
    first_card = context.driver.find_element_by_xpath(element_xpath)
    first_card.click()

@when("the user should be redirect to Amazon (.*)")
def step_impl(context, page):
    context.page = get_page_module(page) 
    assert context.page.url in context.driver.current_url
    
@then('the (.*) should be appear')
def step_impl(context, element):
    element = get_locoter_from_feature(element)
    element_xpath = get_xpath_from_page(context, element)
    left_bar = context.driver.find_element_by_xpath(element_xpath)
    left_bar.is_displayed()

@then('the (.*) should have (.*)')
def step_impl(context, parent_element, child_element):
    """
    check if the text available in parent div 
    """
    parent_element = get_locoter_from_feature(parent_element)
    child_element = get_locoter_from_feature(child_element)    
    parent_xpath = get_xpath_from_page(context, parent_element)
    child_xpath = get_xpath_from_page(context, child_element)
    department_section = context.driver.find_element_by_xpath(parent_xpath + child_xpath)
    department_section.is_displayed()
