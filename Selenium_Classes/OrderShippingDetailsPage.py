from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderShippingDetailsPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def next_click(self):
        # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[translate='Edit_shipping_Details']")))
        self.wait_for_presence_next_button()

        while True:
            try:
                return self.driver.find_element(By.ID, "next_btn").click()
            except:
                pass

    def wait_for_presence_next_button(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "next_btn")))

    def thank_for_order(self):
        """ Return the thank-you text after buying """
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                          "span[translate='Thank_you_for_buying_with_Advantage']")))
        return self.driver.find_element(By.CSS_SELECTOR, "span[translate='Thank_you_for_buying_with_Advantage']").text

    def order_number(self):
        """ Return order number """
        self.wait.until(EC.visibility_of_element_located((By.ID, "orderNumberLabel")))
        return self.driver.find_element(By.ID, "orderNumberLabel").text

    def type_username(self, username: str):
        self.wait.until(EC.presence_of_element_located((By.NAME, "usernameInOrderPayment")))
        self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(username)

    def type_password(self, password: str):
        self.wait.until(EC.presence_of_element_located((By.NAME, "passwordInOrderPayment")))
        self.driver.find_element(By.NAME, "passwordInOrderPayment").send_keys(password)

    def click_login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "login_btnundefined")))
        self.driver.find_element(By.ID, "login_btnundefined").click()

