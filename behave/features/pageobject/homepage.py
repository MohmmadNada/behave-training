from features.pageobject.basepage import * 
class MainPage(BasePage):
    def __init__(self):

        super().__init__()
        self.url =  self.base_url + '/'
        
        # page xpath selectors
        self.first_card = "//div[@data-a-card-type='basic'][1]"
        self.left_side_bar = "//div[@id='s-refinements']"
        self.department_text = '//span[text()="Department"]'
        self.customer_reviews_text = '//span[text()="Customer Reviews"]'
        self.brand_text = '//span[text()="Brand"]'
        self.price_text = '//span[text()="Price"]'
