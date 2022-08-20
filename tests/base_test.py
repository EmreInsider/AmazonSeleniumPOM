import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com/'
    wait_time = 10

    def setUp(self):
        option = Options()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver.exe", chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(self.wait_time)
        self.wait = WebDriverWait(self.driver, self.wait_time)
