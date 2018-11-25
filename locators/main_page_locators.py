from selenium.webdriver.common.by import By


class MainPageLocators(object):
    DOWNLOAD_TAB = (By.CSS_SELECTOR, '.navigation.menu > li > a[href="/downloads/"]')
    GO_BUTTON = (By.ID, 'submit')
