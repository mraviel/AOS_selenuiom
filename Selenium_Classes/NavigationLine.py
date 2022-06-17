from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Navigation_line :
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def click_logo_icon (self):
        self.driver.find_element(By.CSS_SELECTOR, "a[ng-click='go_up()']").click()

    def click_account_icon (self):
        self.wait.until(EC.presence_of_element_located((By.ID,"menuUser")))
        self.driver.find_element(By.ID, "menuUser").click()

    def moucse_hover_cart_icon (self):
        self.wait.until(EC.presence_of_element_located((By.ID, "menuCart")))
        self.action.move_to_element(self.driver.find_element(By.ID, "menuCart"))
        self.action.perform()

    def click_cart_icon (self):
        self.driver.find_element(By.ID, "menuCart").click()

    def cart_icon_product (self):
        self.moucse_hover_cart_icon()
        return self.driver.find_elements(By.TAG_NAME, "tbody")

    def colorandquantity (self, num:int):
        self.moucse_hover_cart_icon()
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td>a>label")))
        return self.driver.find_elements(By.CSS_SELECTOR, "td>a>label")[num].text

    def remove_product_from_cart_icon (self,num=int):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "td>div>div[class='removeProduct iconCss iconX']")))
        self.driver.find_elements(By.CSS_SELECTOR, "td>div>div[class='removeProduct iconCss iconX']")[num].click()

    def my_account_option (self):
        self.click_account_icon()
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div>label[class='option roboto-medium ng-scope']")))
        self.driver.find_element(By.CSS_SELECTOR, "div>label[class='option roboto-medium ng-scope'][translate='My_account']").click()

    def sign_out_option (self):
        self.click_account_icon()
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div>label[class='option roboto-medium ng-scope'][translate='Sign_out']")))
        self.driver.find_element(By.CSS_SELECTOR,"div>label[class='option roboto-medium ng-scope'][translate='Sign_out']").click()










# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class NavigationLine:
#
#     def __init__(self, driver: webdriver.Chrome):
#         self.driver=driver
#         self.wait = WebDriverWait(self.driver, 10)
#         self.action = ActionChains(self.driver)
#
#     def click_logo_icon(self):
#         self.driver.find_element(By.CSS_SELECTOR, "a[ng-click='go_up()']").click()
#
#     def click_account_icon(self):
#         self.wait.until(EC.presence_of_element_located((By.ID, "menuUser")))
#         self.driver.find_element(By.ID, "menuUser").click()
#
#     def mouse_hover_cart_icon(self):
#         self.wait.until(EC.presence_of_element_located((By.ID, "menuCart")))
#         self.action.move_to_element(self.driver.find_element(By.ID, "menuCart"))
#         self.action.perform()
#
#     def click_cart_icon(self):
#         self.driver.find_element(By.ID, "menuCart").click()
#
#     def cart_icon_product(self):
#         self.mouse_hover_cart_icon()
#         return self.driver.find_elements(By.TAG_NAME, "tbody")
