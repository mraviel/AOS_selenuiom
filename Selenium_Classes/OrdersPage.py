from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class OrdersPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def order_numbers(self):
        """ Return all order numbers : list """

        table = self.driver.find_element(By.CSS_SELECTOR, "#myAccountContainer > div > table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        order_numbers = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 3:
                order_numbers.append(cells[0].text)
        return order_numbers
