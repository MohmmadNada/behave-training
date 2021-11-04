from features.pageobject.createaccountpage import CreateAccount
from features.pageobject.basepage import BasePage
from features.pageobject.homepage import HomePage
from features.pageobject.resultpage import ResultPage 
from features.pageobject.signinpage import SignIn

all_pages = {
    "base page": BasePage(),
    "home page": HomePage(),
    "result page": ResultPage(),
    "sign in page": SignIn(),
    "signin page": SignIn(),
    "create account page": CreateAccount()
}
