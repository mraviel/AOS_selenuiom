from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def open_category(self, category: str):
        """ Click on category  """
        category = category.lower()
        self.wait.until(EC.presence_of_element_located((By.ID, f"{category}Txt")))
        self.driver.find_element(By.ID, f"{category}Txt").click()

    def return_SPACIAL_OFFER(self):
        """ Special Offer title in home page """
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[translate='SPACIAL_OFFER']")))
        return self.driver.find_element(By.CSS_SELECTOR, "h3[translate='SPACIAL_OFFER']").text
