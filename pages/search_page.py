from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchPage(BasePage):
    SEARCHED_KEYWORD = (By.CLASS_NAME, 'a-color-state')
    PAGINATION_BTN = '//a[@aria-label="Go to page {}"]'
    SELECTED_PAGINATION = (By.CLASS_NAME, 's-pagination-selected')
    SELECT_THIRD_PRODUCT = (By.TAG_NAME, 'h2')

    product = ""

    def get_searched_keyword_control(self):
        return self.wait_element(self.SEARCHED_KEYWORD).text

    def click_second_pagination_btn(self, page_number):
        self.click_element(By.XPATH, self.PAGINATION_BTN.format(page_number))

    def get_pagination_selected_text(self):
        return self.wait_element(self.SELECTED_PAGINATION).text

    def click_select_third_product(self):
        self.product = self.driver.find_elements(*self.SELECT_THIRD_PRODUCT)[2].text
        self.click_element(By.XPATH, "//span[text()='{}']".format(self.product))

        return ProductPage(self.driver)

    def get_selected_product_name(self):
        return self.product
