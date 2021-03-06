from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *

from Selenium_Classes.NavigationLine import Navigation_line


class ShoppingCart:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.action = ActionChains(self.driver)
        self.navigation_line = Navigation_line(self.driver)

    def logo_shopping_cart(self):
        """ Return the page name """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='select  ng-binding']")))
        return self.driver.find_element(By.CSS_SELECTOR, "a[class='select  ng-binding']").text

    def edit_product_by_index(self, num: int):
        """ Click on edit product """
        while True:
            try:
                self.driver.find_elements(By.CSS_SELECTOR, "span>a[class='edit ng-scope']")[num].click()
                break
            except:
                pass

    def remove_product_by_index(self, num: int):
        """ Click on remove product """
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

    def final_price_from_shoppingcart(self):
        """ Return total price form shopping cart page """
        self.navigation_line.click_cart_icon()
        self.wait.until(EC.presence_of_element_located((By.ID, "checkOutButton")))
        return self.driver.find_element(By.ID, "checkOutButton").text
