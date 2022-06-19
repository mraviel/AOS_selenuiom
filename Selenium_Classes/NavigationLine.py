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
        # self.wait.until(EC.presence_of_element_located((By.ID,"menuUser")))
        self.wait.until(EC.element_to_be_clickable((By.ID,"menuUser")))
        self.driver.find_element(By.ID, "menuUser").click()

    def mouse_hover_cart_icon (self):
        self.wait.until(EC.presence_of_element_located((By.ID, "menuCart")))
        self.action.move_to_element(self.driver.find_element(By.ID, "menuCart"))
        self.action.perform()

    def click_cart_icon(self):
        self.driver.find_element(By.ID, "menuCart").click()

    def cart_icon_product (self):
        self.mouse_hover_cart_icon()
        return self.driver.find_elements(By.TAG_NAME, "tbody")

    def color_and_quantity (self, num:int):
        self.mouse_hover_cart_icon()
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

    def username_appearance(self):
        """ Return username: str,
            From Navigation Line """
        # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='menuUserLink'] > span")))
        self.wait_for_visibility_of_username()
        return self.driver.find_element(By.CSS_SELECTOR, "a[id='menuUserLink'] > span").text

    def account_options_small_window_style(self):
        """ Return the style of account options:
            None=close, block=open"""
        return self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle").get_attribute("style")

    def wait_for_invisibility_of_username(self):
        self.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "a[id='menuUserLink'] > span")))

    def wait_for_visibility_of_username(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='menuUserLink'] > span")))

    def wait_for_invisibility_of_cart_small_windows(self):
        """ Wait for cart small window to disappear """
        self.wait.until(EC.invisibility_of_element((By.ID, "toolTipCart")))

    # def wait_for_visibility_of_account_options(self):
    #     self.wait.until(EC.visibility_of_all_elements_located((By.ID, "menuUser")))

    def click_on_my_orders(self):
        self.click_account_icon()
        # self.wait.until(EC.visibility_of((self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle > label")[1])))
        # self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#loginMiniTitle > label")))
        self.wait_for_invisibility_of_cart_small_windows()
        self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle > label")[1].click()

    def cart_small_window_products(self):
        """ Return all products from cart small window
            [[name, quantity, color, price], [...] ...] """

        self.mouse_hover_cart_icon()
        table = self.driver.find_element(By.CSS_SELECTOR, "div > table")
        rows = table.find_elements(By.CSS_SELECTOR, "tbody > tr")

        products = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            name_color_quantity = cells[1].text
            price = cells[2].text

            t = name_color_quantity.split("\n")
            t.append(price)

            # remove dots
            if " ..." in t[0] and len(t[0]) >= 30:
                t[0] = t[0].replace(" ...", "")
            elif "..." in t[0] and len(t[0]) >= 30:
                t[0] = t[0].replace("...", "")

            products.append(t)  # [name, quantity, color, price]

        return products

    def quantity_from_cart(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[id='shoppingCartLink']>span")))
        return self.driver.find_element(By.CSS_SELECTOR, "a[id='shoppingCartLink']>span").text

    def final_price_from_cart_icon(self):
        self.mouse_hover_cart_icon()
        self.wait.until(EC.presence_of_element_located((By.ID, "checkOutPopUp")))
        return self.driver.find_element(By.ID, "checkOutPopUp").text













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
