from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchPage(BasePage):
    SECOND_PAGINATION_BTN = (By.LINK_TEXT, '2')
    SELECTED_PAGINATION = (By.CLASS_NAME, 's-pagination-selected')
    SELECTED_PRODUCT = (By.XPATH, '(//div[@data-index = 3])[1]//a')

    def click_second_pagination_btn(self):
        self.click_element(*self.SECOND_PAGINATION_BTN)

    def get_pagination_selected_text(self):
        return self.wait_element(self.SELECTED_PAGINATION).text

    def click_selected_product(self, index):
        self.find_elements(index, *self.SELECTED_PRODUCT)

        return ProductPage(self.driver)
