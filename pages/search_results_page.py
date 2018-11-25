import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.search_page_locators import SearchPageLocator
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def should_display_list_of_recent_events(self):
        assert self.element(SearchPageLocator.FIRST_EVENT_TIME).is_displayed()

