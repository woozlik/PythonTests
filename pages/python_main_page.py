from elements.search_field_on_main_page import SearchFieldMainPage
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.download_page import DownloadPage
from pages.search_results_page import SearchResultsPage


class MainPage(BasePage):
    search_text_element = SearchFieldMainPage()

    def is_title_matches(self, title):
        assert title in self.driver.title

    def click_search_button(self):
        self.element(MainPageLocators.GO_BUTTON).click()
        return SearchResultsPage(self.driver)

    def open_page(self):
        self.driver.get('https://www.python.org/')
        return self

    def click_on_downloads_tab(self):
        self.element(MainPageLocators.DOWNLOAD_TAB).click()
        return DownloadPage(self.driver)
