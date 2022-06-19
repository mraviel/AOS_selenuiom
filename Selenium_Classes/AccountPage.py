from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def delete_account_located(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".deleteMainBtnContainer")))
        return self.driver.find_element(By.CSS_SELECTOR, ".deleteMainBtnContainer")

    def click_yes(self):
        # After clicking on delete account
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".deleteRed")))
        self.driver.find_element(By.CSS_SELECTOR, ".deleteRed").click()

    def click_delete_account(self):
        """ Delete Account """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".deleteMainBtnContainer")))
        self.delete_account_located().click()
        self.click_yes()

    def force_delete_account(self):
        """ Force delete account """

        while True:
            try:
                self.click_delete_account()
                break
            except:
                pass


