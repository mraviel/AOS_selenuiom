from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *


class Category_page :

    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def choose_product_by_index (self, num:int):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul>li>img")))
        self.driver.find_elements(By.CSS_SELECTOR, "ul>li>img")[num].click()