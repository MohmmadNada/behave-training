from features.pageobject.basepage import * 

class ResultPage(BasePage):
    def __init__(self):

        super().__init__()
        self.url =  self.base_url + '/' +"s?k="
        
        # page xpath selectors
        self.left_side_bar = "//div[@id='s-refinements']"
        self.department_text = '//span[text()="Department"]'
        self.customer_reviews_text = '//span[text()="Customer Reviews"]'
        self.brand_text = '//span[text()="Brand"]'
        self.price_text = '//span[text()="Price"]'