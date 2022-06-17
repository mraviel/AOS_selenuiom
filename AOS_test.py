
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from os import path

from Selenium_Classes.HomePage import HomePage
from Selenium_Classes.CategoryPage import Category_page
from Selenium_Classes.ProductPage import Product_page
from Selenium_Classes.NavigationLine import Navigation_line


class TestAOS(TestCase):

    def setUp(self):
        # PATH
        driver_folder = path.join(path.dirname(__file__), 'Driver')
        chrome_driver_path = path.join(path.join(driver_folder, 'chromedriver'))

        service_chrome = Service(chrome_driver_path)

        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        self.home_page = HomePage(self.driver)
        self.category_page = Category_page(self.driver)
        self.product_page = Product_page(self.driver)
        self.navigation_line = Navigation_line(self.driver)

    def test_num2(self):

        self.home_page.open_speakers_category()
        self.category_page.choose_product_by_index(1)
        self.product_page.choose_Quantity(2)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        self.home_page.open_mice_category()
        self.category_page.choose_product_by_index(3)
        self.product_page.choose_Quantity(1)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        self.home_page.open_laptops_category()
        self.category_page.choose_product_by_index(0)
        self.product_page.choose_Quantity(3)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()



    def tearDown(self):
        # Close the test
        sleep(4)
        self.driver.close()

