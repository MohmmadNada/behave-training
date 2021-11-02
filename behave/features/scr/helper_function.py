from features.scr.all_opject import *
def get_locoter_from_feature(locator):
    """
    takes locator from feature statement, replace space with underscore and make all characters in lowercase
    """
    return locator.lower().replace(" ", "_")

def get_xpath_from_page(context, locator):
    """
    takes page module and locator name and return xpath locator"""
    locator = locator.lower().replace(" ", "_")
    return  context.page.__getattribute__(locator)

def get_page_module(page):
    try: 
        return all_pages[page.lower()]
    except KeyError:
        raise KeyError(f"{page} is not available, please check the page name")

