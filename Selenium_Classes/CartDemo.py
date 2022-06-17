from selenium import webdriver
from selenium.webdriver.common.by import By


# DELETE ME

class DemoCart:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkOutButton").click()
