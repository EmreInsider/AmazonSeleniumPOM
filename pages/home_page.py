from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage


class HomePage(BasePage):
    LOGIN_PAGE_BTN = (By.ID, "nav-link-accountList")
    SEARCH_TEXT_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait_element(self.LOGIN_PAGE_BTN, 'There is no login page button on the page !')
        self.wait_element(self.SEARCH_BTN, 'There is no search button on the page !')

    def click_login_page_btn(self):
        self.click_element(*self.LOGIN_PAGE_BTN)

        return LoginPage(self.driver)

    def fill_search_text_box(self, text):
        self.send_text(text, *self.SEARCH_TEXT_BOX)

    def click_search_btn(self):
        self.click_element(*self.SEARCH_BTN)

        return SearchPage(self.driver)
