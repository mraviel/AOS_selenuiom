from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def account_icon(self):
        # DELETE ME
        return self.driver.find_element(By.ID, "menuUser")

    def username(self):
        # Wait until element located
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        return self.driver.find_element(By.NAME, "username")

    def password(self):
        # Wait until element located
        self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        return self.driver.find_element(By.NAME, "password")

    def signin(self):
        while True:
            try:
                self.driver.find_element(By.ID, "sign_in_btnundefined").click()
                break
            except:
                pass

    def click_new_account(self):
        # Wait until element located
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[translate='CREATE_NEW_ACCOUNT']")))
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, "a[translate='CREATE_NEW_ACCOUNT']").click()
                break
            except:
                pass

    def type_username(self, username: str):
        # Wait until element located
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        self.username().send_keys(username)  # Exel

    def type_password(self, password: str):
        # Wait until element located
        self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        self.password().send_keys(password)  # Exel

