class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def element(self, locator):
        return self.driver.find_element(*locator)
