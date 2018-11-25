import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.python_main_page import MainPage


class PythonSiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_verify_title(self):
        driver = self.driver
        main_page = MainPage(self.driver).open_page()
        main_page.is_title_matches("Python")

        assert "No results found." not in driver.page_source

    def test_search_in_python_org(self):
        main_page = MainPage(self.driver).open_page()
        main_page.search_text_element = "pycon"
        search_results_page = main_page.click_search_button()
        search_results_page.should_display_list_of_recent_events()

    def test_download_page_display_release_table(self):
        main_page = MainPage(self.driver).open_page()
        download_page = main_page.click_on_downloads_tab()
        download_page.should_display_release_table()

    def tearDown(self):
        self.driver.close()
