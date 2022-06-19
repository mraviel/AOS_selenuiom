from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Category_page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def choose_product_by_index(self, num: int):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul>li>img")))
        self.driver.find_elements(By.CSS_SELECTOR, "ul>li>img")[num].click()

    def choose_product_by_id(self, id: int):
        self.wait.until(EC.presence_of_element_located((By.ID, f"{id}")))
        self.driver.find_element(By.ID, f"{id}").click()

    def page_name(self):
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "h3[class='categoryTitle roboto-regular sticky ng-binding']")))
        return self.driver.find_element(By.CSS_SELECTOR, "h3[class='categoryTitle roboto-regular sticky ng-binding']").text
