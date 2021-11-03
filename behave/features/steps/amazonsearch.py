from behave import * 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.environment import *
from features.pageobject.homepage import *
from features.scr.helper_function import *
use_step_matcher("re")


@when(u'type (.*) in (.*) field')
def type_in_field(context, search_text, locator):
    
    input_field = get_element_from_feature(context, locator)
    input_field.clear()
    input_field.send_keys(search_text)

@when(u'click on (.*)')
def click_on(context, locator):

    first_card = get_element_from_feature(context, locator)
    first_card.click()


@then(u'The result page url should have (.*) word')
def test_url_contain(context, search_word):
    assert search_word in context.driver.current_url 
