def get_locoter_from_feature(locator):
    """
    takes locator from feature statement, replace space with underscore and make all characters in lowercase
    """
    return locator.lower().replace(" ", "_")
def get_xpath_from_page(page_obj, locator):
    """
    takes page module and locator name and return xpath locator"""
    return  page_obj.__getattribute__(locator)
