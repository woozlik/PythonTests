from selenium.webdriver.common.by import By


class SearchPageLocator(object):
    LIST_OF_RECENT_EVENTS = (By.CSS_SELECTOR, '.list-recent-events.menu')
    MAIN_CONTENT = (By.CSS_SELECTOR, '.main-content')
    FIRST_EVENT_TIME = (By.CSS_SELECTOR, '.list-recent-events.menu p time')

