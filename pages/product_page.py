from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.wish_list_page import WishListPage


class ProductPage(BasePage):
    ADD_TO_WISH_LIST_BTN = (By.ID, 'add-to-wishlist-button-submit')
    VIEW_YOUR_LIST_BTN = (By.CSS_SELECTOR, '#huc-view-your-list-button .a-button-inner')

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait_element(self.ADD_TO_WISH_LIST_BTN, 'There is no add to wish list button on the page !')

    def click_add_to_wish_list_btn(self):
        self.click_element(*self.ADD_TO_WISH_LIST_BTN)

    def click_view_your_list_btn(self):
        self.click_element(*self.VIEW_YOUR_LIST_BTN)

        return WishListPage(self.driver)
