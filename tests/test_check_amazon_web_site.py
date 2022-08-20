from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCheckAmazonSite(BaseTest):
    email = "19emrclk07@gmail.com"
    password = "Abc.112233"
    search_input_text = "samsung"
    index_item = 1
    page_number = "2"

    def test_check_amazon_site(self):
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_url(), self.base_url, 'This page is not the homepage !')

        login_page = home_page.click_login_page_btn()
        login_page.fill_email_text_box(self.email)
        login_page.click_continue_btn()
        login_page.fill_password_text_box(self.password)
        login_page.click_submit_btn()

        home_page.fill_search_text_box(self.search_input_text)

        search_page = home_page.click_search_btn()
        self.assertIn(self.search_input_text, search_page.get_searched_keyword_control(),
                      "This page is not {} search page !".format(self.search_input_text))
        search_page.click_second_pagination_btn(self.page_number)
        self.assertTrue(search_page.get_pagination_selected_text(), 'This page is not the second page !')

        product_page = search_page.click_select_third_product()
        product_page.click_add_to_wish_list_btn()

        wish_list_page = product_page.click_view_your_list_btn()
        self.assertEqual(search_page.get_selected_product_name(), wish_list_page.is_present_wish_list_item(),
                         'Added product does not match !')
        wish_list_page.click_item_remove_btn()
        self.assertTrue(wish_list_page.get_empty_wish_list_page_text(), 'Added product not removed from wishList !')

    def tearDown(self):
        self.driver.quit()
