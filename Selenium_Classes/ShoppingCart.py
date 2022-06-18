from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *


class ShoppingCart:

    def __init__(self, driver: webdriver.Chrome):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 20)
        self.action = ActionChains(self.driver)

    def logo_shopping_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='select  ng-binding']")))
        return self.driver.find_element(By.CSS_SELECTOR, "a[class='select  ng-binding']").text

    def edit_product_by_index(self, num: int):
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span>a[class='edit ng-scope']")))
        while True:
            try:
                self.driver.find_elements(By.CSS_SELECTOR, "span>a[class='edit ng-scope']")[num].click()
                break
            except:
                pass

    def remove_product_by_index(self, num: int):
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span>a[class='edit ng-scope']")))
        while True:
            try:
                self.driver.find_elements(By.CSS_SELECTOR, "span>a[class='remove red ng-scope']")[num].click()
                break
            except:
                pass

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkOutButton").click()

    def all_shopping_cart_items(self):
        """ Return all shopping cart items
            [[name, quantity, price], [name, quantity, price] ...] """

        table = self.driver.find_element(By.CSS_SELECTOR, "table.fixedTableEdgeCompatibility")
        rows = table.find_elements(By.CSS_SELECTOR, "tbody > tr")  # Only the items in the body section
        all_items = []
        for row in rows:
            item = []
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                item.append(cell.text)
            item = [x for x in item if x]  # Remove all empty item values ('')
            item[2] = item[2][0:-14]  # Remove additional words from price
            all_items.append(item)

        return all_items

    def continue_shopping(self):
        """ Return  """
        # EDIT ME
        return self.driver.find_element(By.LINK_TEXT, "CONTINUE SHOPPING").text
