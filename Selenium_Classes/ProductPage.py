from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *


class Product_page:

    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def choose_color (self, str:str):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[ng-show='firstImageToShow']>span[title='{str}']")))
        self.driver.find_element(By.CSS_SELECTOR, f"div[ng-show='firstImageToShow']>span[title='{str}']").click()

    def choose_Quantity (self, num:int):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"input[name='quantity']")))
        self.driver.find_element(By.CSS_SELECTOR, f"input[name='quantity']").click()
        self.driver.find_element(By.CSS_SELECTOR, f"input[name='quantity']").send_keys(num)

    def click_on_att_to_cart (self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='save_to_cart']")))
        self.driver.find_element(By.CSS_SELECTOR, "[name='save_to_cart']").click()

    def get_product_name(self):
        """ Return text of product name """
        return self.driver.find_element(By.CSS_SELECTOR, "div#Description > h1").text

    def get_product_price(self):
        """ Return text of product price """
        return self.driver.find_element(By.CSS_SELECTOR, "div#Description > h2").text

    def get_product_color(self):
        """ Return title of selected color """
        return self.driver.find_element(By.CSS_SELECTOR, "div > span.colorSelected").get_attribute("title")

    def get_product_quantity(self):
        """ Return value of product quantity """
        return self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']").get_attribute("value")

    def get_product_info(self):
        """ Return list: [name, quantity, color, price] """
        name = self.get_product_name()
        price = self.get_product_price()
        quantity = self.get_product_quantity()
        color = self.get_product_color()

        return [name, quantity, color, price]
