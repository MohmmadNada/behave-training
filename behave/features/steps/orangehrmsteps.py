# from behave import given
from behave import *
from selenium import webdriver
@given('launch chrome browser')
def launchBrowser(context):
    # context.driver=webdriver.Chrome('/usr/local/bin/chromedriver')
    context.driver=webdriver.Chrome()

@when('open orange hrm home page')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
    assert status is True
    # //body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]


@then('close browser')
def closeBrowser(context):
    context.driver.close()
