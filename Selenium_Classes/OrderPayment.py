from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class OrderPayment:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # Shipping
    def next_click(self):
        """ Shipping window next click """
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

    # Payment
    def payment_method(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[ng-init='checkedRadio = 1'] > div")

    def choose_payment_method(self, payment_type: str):
        """ Payment name become index """
        # Wait until element located
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[ng-init='checkedRadio = 1'] > div")))

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
        self.driver.find_element(By.ID, "creditCard").send_keys(card_number)

    def clear_credit_cvv_number(self):
        self.driver.find_element(By.NAME, "cvv_number").clear()

    def type_credit_cvv_number(self, cvv: str):
        """ Insert credit cvv twice """
        self.driver.find_element(By.NAME, "cvv_number").send_keys(cvv)
        self.clear_credit_cvv_number()
        self.driver.find_element(By.NAME, "cvv_number").send_keys(cvv)

    def credit_expiration_date_mm(self, mm: str):
        element = Select(self.driver.find_element(By.NAME, "mmListbox"))
        element.select_by_visible_text(mm)

    def credit_expiration_date_yy(self, yy: str):
        element = Select(self.driver.find_element(By.NAME, "yyyyListbox"))
        element.select_by_visible_text(yy)

    def type_credit_cardholder(self, cardholder: str):
        self.driver.find_element(By.NAME, "cardholder_name").send_keys(cardholder)

    def credit_pay_now_click(self):
        self.driver.find_element(By.ID, "pay_now_btn_ManualPayment").click()

    def click_registration(self):
        self.driver.find_element(By.ID, "registration_btnundefined").click()

    # Login via order payment page
    def type_username(self, username: str):
        self.wait.until(EC.presence_of_element_located((By.NAME, "usernameInOrderPayment")))
        self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(username)

    def type_password(self, password: str):
        self.wait.until(EC.presence_of_element_located((By.NAME, "passwordInOrderPayment")))
        self.driver.find_element(By.NAME, "passwordInOrderPayment").send_keys(password)

    def click_login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "login_btnundefined")))
        self.driver.find_element(By.ID, "login_btnundefined").click()