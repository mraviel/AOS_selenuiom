from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *


class HomePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def open_speakers_category (self):
        self.wait.until(EC.presence_of_element_located((By.ID, "speakersTxt")))
        self.driver.find_element(By.ID , "speakersTxt").click()

    def open_tablets_category (self):
        self.wait.until(EC.presence_of_element_located((By.ID, "tabletsTxt")))
        self.driver.find_element(By.ID, "tabletsTxt").click()

    def open_laptops_category(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "laptopsTxt")))
        self.driver.find_element(By.ID, "laptopsTxt").click()

    def open_mice_category(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "miceTxt")))
        self.driver.find_element(By.ID, "miceTxt").click()

    def open_headphones_category(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "headphonesTxt")))
        self.driver.find_element(By.ID, "headphonesTxt").click()

    def open_category(self, category: str):

        category = category.lower()
        self.wait.until(EC.presence_of_element_located((By.ID, f"{category}Txt")))
        self.driver.find_element(By.ID, f"{category}Txt").click()

    def return_SPACIAL_OFFER(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[translate='SPACIAL_OFFER']")))
        return self.driver.find_element(By.CSS_SELECTOR, "h3[translate='SPACIAL_OFFER']").text
