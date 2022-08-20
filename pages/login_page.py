import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_TEXT_BOX = (By.ID, "ap_email")
    CONTINUE_BTN = (By.ID, "continue")
    PASSWORD_TEXT_BOX = (By.ID, "ap_password")
    SUBMIT_BTN = (By.ID, "signInSubmit")

    def fill_email_text_box(self, email):
        self.send_text(email, *self.EMAIL_TEXT_BOX)

    def click_continue_btn(self):
        self.click_element(*self.CONTINUE_BTN)

    def fill_password_text_box(self, password):
        time.sleep(2)
        self.send_text(password, *self.PASSWORD_TEXT_BOX)

    def click_submit_btn(self):
        self.click_element(*self.SUBMIT_BTN)
