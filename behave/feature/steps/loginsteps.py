from behave import * 
from selenium import webdriver

@given('I launch Chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()

@when('I open Orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

# user: admin, password:  admin123
# The single and double quotes is important 
@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_id('txtUsername').send_keys(user)
    context.driver.find_element_by_id('txtPassword').send_keys(pwd)    

@when('Click on Login button')
def step_impl(context):
    context.driver.find_element_by_id('btnLogin').click()

@then('User must successfully login to dashboard page')
def step_impl(context):
    # text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]")
    try:
        text = context.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
    except:
        print("here have issue in find text, we will close the browser")
        context.driver.close()
        assert False, "Text failed"
    if text ==  "Dashboard":
        context.driver.close()
        assert True,"Test passed"
    
    
# //h1[contains(text(),'Dashboard')]