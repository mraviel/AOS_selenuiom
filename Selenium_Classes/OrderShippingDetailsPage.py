from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderShippingDetailsPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 10)

    def next_click(self):
        # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[translate='Edit_shipping_Details']")))

        while True:
            try:
                return self.driver.find_element(By.ID, "next_btn").click()
            except:
                pass






