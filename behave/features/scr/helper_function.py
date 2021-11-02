def get_locoter_from_feature(locator):
    """
    takes locator from feature statement, replace space with underscore and make all characters in lowercase
    """
    return locator.lower().replace(" ", "_")
