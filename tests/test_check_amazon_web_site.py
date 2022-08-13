import time

from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCheckAmazonSite(BaseTest):
    email = "19emrclk07@gmail.com"
    password = "Abc.112233"
    search_input_text = "samsung"
    index_item = 1
    deleted_text_message = 'Deleted'

    def test_check_amazon_site(self):
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_url(), self.base_url, 'This page is not the homepage !')

        login_page = home_page.click_login_page_btn()
        login_page.fill_email_text_box(self.email)
        login_page.click_continue_btn()
        login_page.fill_password_text_box(self.password)
        time.sleep(3)
        login_page.click_submit_btn()

        home_page.fill_search_text_box(self.search_input_text)

        search_page = home_page.click_search_btn()
        search_page.click_second_pagination_btn()
        self.assertTrue(search_page.get_pagination_selected_text(), 'This page is not the second page !')

        product_page = search_page.click_selected_product(self.index_item)
        product_page.click_add_to_wish_list_btn()

        wish_list_page = product_page.click_view_your_list_btn()
        self.assertTrue(wish_list_page.is_present_wish_list_item(), 'There are no products on the wish list page !')
        wish_list_page.click_item_remove_btn()
        self.assertTrue(wish_list_page.is_present_wish_list_item(), 'Wish list page is not empty !')
        self.assertEqual(self.deleted_text_message, wish_list_page.get_empty_wish_list_page_text(),
                         'There are still product on the wish list page !')

    def tearDown(self):
        self.driver.quit()
