from features.pageobject.basepage import * 
class HomePage(BasePage):
    def __init__(self):

        super().__init__()
        self.url =  self.base_url + '/'
        
        # page xpath selectors
        self.first_card = "//div[@data-a-card-type='basic'][1]"
        self.search_input = "//input[@id='twotabsearchtextbox']"
        self.search_button = "//input[@id='nav-search-submit-button']"
        self.sign_in_button = "//div[@id='nav-signin-tooltip']"
        
        # self.continue_button = ''
