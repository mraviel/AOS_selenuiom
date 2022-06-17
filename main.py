from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from os import path
from random import choice
from Selenium_Classes.LoginPage import LoginPage
from Selenium_Classes.SignupPage import SignupPage
from Selenium_Classes.CartDemo import DemoCart
from Selenium_Classes.NavigationLine import NavigationLine
from Selenium_Classes.OrderShippingDetailsPage import OrderShippingDetailsPage
from Selenium_Classes.OrderPaymentMethod import OrderPaymentDetails

from openpyxl import load_workbook


# PATH
driver_folder = path.join(path.dirname(__file__), 'Driver')
chrome_driver_path = path.join(path.join(driver_folder, 'chromedriver'))

service_chrome = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service_chrome)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

driver.implicitly_wait(10)

login_page = LoginPage(driver)
register_page = SignupPage(driver)
navigation_page = NavigationLine(driver)
cart_page = DemoCart(driver)
shipping_details_page = OrderShippingDetailsPage(driver)
payment_details_page = OrderPaymentDetails(driver)


login_page.account_icon().click()

login_page.account_icon()
login_page.type_username("aviel123")
login_page.type_password("Aviel123")
login_page.signin()
sleep(3)

navigation_page.click_cart_icon()
cart_page.click_checkout()

shipping_details_page.next_click()

payment_details_page.choose_payment_method("MasterCredit")
payment_details_page.type_credit_card_number("123456789123")
payment_details_page.type_credit_cvv_number("1233")
payment_details_page.credit_expiration_date_mm("09")
payment_details_page.credit_expiration_date_yy("2024")
payment_details_page.type_credit_cardholder("aviel")
payment_details_page.credit_pay_now_click()









