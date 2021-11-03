from features.scr.all_opjects import *

def get_locoter_from_feature(locator):
    """
    takes locator from feature statement, return locator in selectors format
    """
    return locator.lower().replace(" ", "_")

def get_xpath_from_page(context, locator):
    """
    takes locator from feature statement and return xpath
    """
    locator = locator.lower().replace(" ", "_")
    return  context.page.__getattribute__(locator)

def get_page_module(page):
    """
    takes page name from feature statement and return page module instance  
    """
    try: 
        return all_pages[page.lower()]
    except KeyError:
        raise KeyError(f"{page} is not available, please check the page name")

def get_element_by_xpath(context, locator):
    """
    takes locator from feature statement and return xpath 
    """
    return context.driver.find_element_by_xpath(locator)

def get_element_from_feature(context, locator):
    """
    takes locator from feature statement, return element
    """
    locator = locator.lower().replace(" ", "_")
    xpath_locator = context.page.__getattribute__(locator)
    return context.driver.find_element_by_xpath(xpath_locator)

def visit_page(context, url):
    """
    takes url page, visit url page
    """
    return context.driver.get(context.page.url)

def get_element_inside_element(context, parent_locator, child_locator):
    """
    takes parent and child locator from feature statement, return element
    """
    xpath_parent = get_xpath_from_page(context, parent_locator)
    xpath_child = get_xpath_from_page(context, child_locator)
    return context.driver.find_element_by_xpath(xpath_parent  + xpath_child )