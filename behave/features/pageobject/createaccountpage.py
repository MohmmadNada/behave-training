from features.pageobject.basepage import * 
class CreateAccount(BasePage):
    def __init__(self):

        super().__init__()
        self.url =  self.base_url + '/' # how can I know the sign in link ?
        self.url_key_word = "register"
        # page xpath selectors
        self.register_form = "//form[@id='ap_register_form']"
        self.user_name = "//input[@id='ap_customer_name']"
        self.user_email = "//input[@id='ap_email']"
        self.user_password = "//input[@id='ap_password']"
        self.user_password_matcher = "//input[@id='ap_password_check']"
        self.continue_button = "//input[@id='continue']"
        # self.continue_button = "//input[@type='submit'] | //input[@id='continue']"
        self.name_alert = "//*[contains(text(),'Enter your name')]"
        self.email_alert = "//*[contains(text(),'Enter your email')]"
        self.password_alert = "//*[contains(text(),'Minimum 6 characters required')]"
        self.invaild_email_alert = "//*[contains(text(),'Invalid email')]"
        self.match_password_alert = "//*[contains(text(),'Passwords must match')]"

