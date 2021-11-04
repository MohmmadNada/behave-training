from features.pageobject.basepage import * 
class SignIn(BasePage):
    def __init__(self):

        super().__init__()
        self.url =  self.base_url + '/' # how can I know the sign in link ?
        
        # page xpath selectors
        self.sign_word ="//h1[contains(text(), 'Sign')]"
        self.create_account_button = '//*[contains(text(), "Create")]'