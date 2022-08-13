from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishListPage(BasePage):
    WISH_LIST_ITEM = (By.XPATH, '//*[contains(@class, "itemImage")]')
    ITEM_REMOVE_BTN = (By.NAME, 'submit.deleteItem')
    DELETED_TEXT = (By.CLASS_NAME, 'a-alert-inline-success')

    def is_present_wish_list_item(self):
        return self.find_element(*self.WISH_LIST_ITEM)

    def click_item_remove_btn(self):
        self.click_element(*self.ITEM_REMOVE_BTN)

    def get_empty_wish_list_page_text(self):
        return self.wait_element(self.DELETED_TEXT).text
