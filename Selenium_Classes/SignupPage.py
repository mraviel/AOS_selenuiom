from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SignupPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def type_username(self, username: str):
        self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(username)

    def type_email(self, email: str):
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(email)

    def type_password(self, password: str):
        self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(password)

    def type_confirm_password(self, confirm_password: str):
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(confirm_password)

    def type_first_name(self, first_name: str):
        self.driver.find_element(By.NAME, "first_nameRegisterPage").send_keys(first_name)

    def type_last_name(self, last_name: str):
        self.driver.find_element(By.NAME, "last_nameRegisterPage").send_keys(last_name)

    def type_phone_number(self, phone_number: str):
        self.driver.find_element(By.NAME, "phone_numberRegisterPage").send_keys(phone_number)

    def type_country(self, country: str):  # Country
        # Try insert country otherwise pass
        try:
            element = Select(self.driver.find_element(By.NAME, "countryListboxRegisterPage"))
            element.select_by_value(country)
        except:
            pass

    def type_city(self, city: str):
        self.driver.find_element(By.NAME, "cityRegisterPage").send_keys(city)

    def type_address(self, address: str):
        self.driver.find_element(By.NAME, "addressRegisterPage").send_keys(address)

    def type_state_region(self, state_region: str):
        self.driver.find_element(By.NAME, "state_/_province_/_regionRegisterPage").send_keys(state_region)

    def type_postal_code(self, postal_code: str):
        self.driver.find_element(By.NAME, "postal_codeRegisterPage").send_keys(postal_code)

    def click_i_agree(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']").click()

    def click_register(self):
        self.driver.find_element(By.CSS_SELECTOR, "#register_btnundefined").click()
