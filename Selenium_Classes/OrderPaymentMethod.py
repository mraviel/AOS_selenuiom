from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPaymentDetails:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def payment_method(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[ng-init='checkedRadio = 1'] > div")

    def choose_payment_method(self, payment_type: str):
        # Wait until element located
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[ng-init='checkedRadio = 1'] > div")))

        d = {"SafePay": 0, "MasterCredit": 1}
        if payment_type not in d.keys():
            raise ValueError("This method get only: 'SafePay' and 'MasterCredit'")
        self.payment_method()[d[payment_type]].click()

    def type_safe_pay_username(self, username: str):
        # Wait until element located
        self.wait.until(EC.presence_of_element_located((By.NAME, "safepay_username")))

        self.driver.find_element(By.NAME, "safepay_username").send_keys(username)

    def type_safe_pay_password(self, password: str):
        # Wait until element located
        self.wait.until(EC.presence_of_element_located((By.NAME, "safepay_password")))

        self.driver.find_element(By.NAME, "safepay_password").send_keys(password)

    def safe_pay_pay_now_click(self):
        # Wait until element located
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pay_now_btn_SAFEPAY")))

        self.driver.find_element(By.CSS_SELECTOR, "#pay_now_btn_SAFEPAY").click()

    def type_credit_card_number(self, card_number: str):
        # must have 16 but 12
        self.driver.find_element(By.ID, "creditCard").send_keys(card_number)

    def clear_credit_cvv_number(self):
        self.driver.find_element(By.NAME, "cvv_number").clear()

    def type_credit_cvv_number(self, cvv: str):
        # if len(cvv) != 3:
        #     raise ValueError("CVV must have 3 numbers init")
        self.clear_credit_cvv_number()
        self.driver.find_element(By.NAME, "cvv_number").send_keys(cvv)

    def credit_expiration_date_mm(self, mm: str):
        element = Select(self.driver.find_element(By.NAME, "mmListbox"))
        print(element)
        element.select_by_visible_text(mm)

    def credit_expiration_date_yy(self, yy: str):
        element = Select(self.driver.find_element(By.NAME, "yyyyListbox"))
        print(element)
        element.select_by_visible_text(yy)

    def type_credit_cardholder(self, cardholder: str):
        self.driver.find_element(By.NAME, "cardholder_name").send_keys(cardholder)

    def credit_pay_now_click(self):
        self.driver.find_element(By.ID, "pay_now_btn_ManualPayment").click()



"""
    def waiting(self, by: tuple):
        self.wait.until(EC.presence_of_element_located(by))
"""




