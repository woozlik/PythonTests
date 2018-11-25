from locators.download_page_locators import DownloadPageLocators
from pages.base_page import BasePage


class DownloadPage(BasePage):
    def should_display_release_table(self):
        assert self.element(DownloadPageLocators.RELEASE_TABLE).is_displayed()






