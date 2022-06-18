from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from os import path

from Selenium_Classes.HomePage import HomePage
from Selenium_Classes.CategoryPage import Category_page
from Selenium_Classes.ProductPage import Product_page
from Selenium_Classes.NavigationLine import Navigation_line
from Selenium_Classes.SignupPage import SignupPage
from Selenium_Classes.LoginPage import LoginPage
from Selenium_Classes.AccountPage import AccountPage
from Selenium_Classes.ShoppingCart import ShoppingCart
from Selenium_Classes.OrderPaymentMethod import OrderPaymentDetails
from Selenium_Classes.OrderShippingDetailsPage import OrderShippingDetailsPage
from Selenium_Classes.OrdersPage import OrdersPage


class TestAOS(TestCase):

    def setUp(self):
        # PATH
        driver_folder = path.join(path.dirname(__file__), 'Driver')
        chrome_driver_path = path.join(path.join(driver_folder, 'chromedriver'))

        service_chrome = Service(chrome_driver_path)

        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        self.home_page = HomePage(self.driver)
        self.category_page = Category_page(self.driver)
        self.product_page = Product_page(self.driver)
        self.navigation_line = Navigation_line(self.driver)
        self.signup_page = SignupPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)
        self.order_payment_details_page = OrderPaymentDetails(self.driver)
        self.order_shipping_details_page = OrderShippingDetailsPage(self.driver)
        self.order_page = OrdersPage(self.driver)

    def test_num2(self):
        """ Test that shopping cart small window to have all correct products that the user added
            matching: product name, color, quantity and price """

        products_info = []  # Gather products info form product page

        # Add first product to cart
        self.home_page.open_speakers_category()
        self.category_page.choose_product_by_id(25)
        self.product_page.choose_Quantity(2)
        products_info.append(self.product_page.get_product_info())  # All info about product
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        # Add second product to cart
        self.home_page.open_mice_category()
        self.category_page.choose_product_by_id(30)
        self.product_page.choose_Quantity(1)
        products_info.append(self.product_page.get_product_info())  # All info about product
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        # Add third product to cart
        self.home_page.open_laptops_category()
        self.category_page.choose_product_by_id(9)
        self.product_page.choose_Quantity(3)
        products_info.append(self.product_page.get_product_info())  # All info about product
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        products_in_cart_window = self.navigation_line.cart_small_window_products()
        products_in_cart_window.reverse()

        # Is product name (part name) in full name
        index = 0
        for product in products_in_cart_window:
            self.assertIn(product[0], products_info[index][0])
            print(f"{product[0]} in '{products_info[index][0]}'")
            index += 1

        # Is quantity, color and price expectation equal to products_in_cart_window?
        info = 1
        while info < 4:
            index = 0
            for product in products_in_cart_window:
                self.assertIn(products_info[index][info], product[info])
                print(f"{products_info[index][info]} in '{product[info]}'")
                index += 1
            info += 1  # what part of the data to test (color, price ...)

    def test4(self):
        """ Test after adding to cart one product navigate to cart page """

        # Add one product to shopping cart
        self.home_page.open_speakers_category()
        self.category_page.choose_product_by_id(25)
        self.product_page.choose_Quantity(2)
        self.product_page.click_on_att_to_cart()

        # Check current location, shopping cart
        self.navigation_line.click_cart_icon()
        current_page_text = self.shopping_cart_page.logo_shopping_cart()
        self.assertEqual("SHOPPING CART", current_page_text)

    def test6(self):
        """ Test that cart page update after editing two products from cart page """

        # Add first product to shopping cart
        self.home_page.open_speakers_category()
        self.category_page.choose_product_by_id(25)
        self.product_page.choose_Quantity(2)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        # Add second product to shopping cart
        self.home_page.open_mice_category()
        self.category_page.choose_product_by_id(30)
        self.product_page.choose_Quantity(1)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        # change first product quantity
        self.navigation_line.click_cart_icon()
        cart_before_change = self.shopping_cart_page.all_shopping_cart_items()

        self.navigation_line.click_cart_icon()
        self.shopping_cart_page.edit_product_by_index(0)
        self.product_page.choose_Quantity(4)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        # change second product quantity
        self.navigation_line.click_cart_icon()
        self.shopping_cart_page.edit_product_by_index(1)
        self.product_page.choose_Quantity(3)
        self.product_page.click_on_att_to_cart()

        self.navigation_line.click_cart_icon()
        cart_after_change = self.shopping_cart_page.all_shopping_cart_items()
        print(cart_after_change)

        # Check if quantity of first product change to 3
        self.assertEqual(cart_after_change[0][1], '3')

        # Check if quantity of second product change to 4
        self.assertEqual(cart_after_change[1][1], '4')

    def test_num8(self):
        """ Test making an order with safe-pay,
            test perches complete, cart is empty and order in order page """

        # Add to cart few products
        self.home_page.open_speakers_category()
        self.category_page.choose_product_by_id(25)
        self.product_page.choose_Quantity(2)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        self.home_page.open_mice_category()
        self.category_page.choose_product_by_id(30)
        self.product_page.choose_Quantity(1)
        self.product_page.click_on_att_to_cart()
        self.navigation_line.click_logo_icon()

        self.navigation_line.click_cart_icon()
        self.shopping_cart_page.click_checkout()

        self.order_payment_details_page.click_registration()

        # Fill info
        self.signup_page.type_username("aviel124")
        self.signup_page.type_email("aviel@gmail.com")
        self.signup_page.type_password("Aviel123")
        self.signup_page.type_confirm_password("Aviel123")
        self.signup_page.type_first_name("aviel")
        self.signup_page.type_last_name("mala")
        self.signup_page.type_phone_number("12345")
        self.signup_page.type_country("Isreal")
        self.signup_page.type_city("Netania")
        self.signup_page.type_address("DR")
        self.signup_page.type_state_region("azorim")
        self.signup_page.type_postal_code("2123")
        self.signup_page.click_i_agree()
        self.signup_page.click_register()

        # self.order_shipping_details_page.wait_for_visibility_next_button()
        self.order_shipping_details_page.next_click()
        self.order_payment_details_page.choose_payment_method("SafePay")
        self.order_payment_details_page.type_safe_pay_username("aviel")
        self.order_payment_details_page.type_safe_pay_password("Aviel123")
        self.order_payment_details_page.safe_pay_pay_now_click()

        # verify the reservation done
        thank_you_massage = self.order_shipping_details_page.thank_for_order()
        order_number = self.order_shipping_details_page.order_number()
        self.assertEqual("Thank you for buying with Advantage", thank_you_massage)

        # Verify shopping cart empty
        self.navigation_line.click_cart_icon()
        shopping_cart_items = self.shopping_cart_page.all_shopping_cart_items()
        self.assertEqual([], shopping_cart_items)

        # Verify order in orders page
        self.navigation_line.click_on_my_orders()
        order_numbers = self.order_page.order_numbers()
        self.assertIn(order_number, order_numbers)

        # Delete the account
        self.navigation_line.my_account_option()
        # self.account_page.click_delete_account()
        self.account_page.force_delete_account()
        print("Account Deleted")

    def test_num10(self):
        """ Test login and logout successfully  """

        # Navigate to register page
        self.navigation_line.click_account_icon()
        self.login_page.click_new_account()

        # Fill info
        self.signup_page.type_username("aviel12")
        self.signup_page.type_email("aviel@gmail.com")
        self.signup_page.type_password("Aviel123")
        self.signup_page.type_confirm_password("Aviel123")
        self.signup_page.type_first_name("aviel")
        self.signup_page.type_last_name("mala")
        self.signup_page.type_phone_number("12345")
        self.signup_page.type_country("Isreal")
        self.signup_page.type_city("Netania")
        self.signup_page.type_city("DR")
        self.signup_page.type_state_region("azorim")
        self.signup_page.type_postal_code("2123")
        self.signup_page.click_i_agree()
        self.signup_page.click_register()

        # Login
        self.navigation_line.click_account_icon()
        self.login_page.type_username("aviel12")
        self.login_page.type_password("Aviel123")
        self.login_page.signin()

        # Is username beside account icon ?
        located_username = self.navigation_line.username_appearance()
        self.assertEqual("aviel12", located_username)

        # Is user can access account page ?
        self.navigation_line.my_account_option()

        # Make sure account page open
        self.account_page.delete_account_located()
        self.assertEqual(self.driver.current_url, "https://www.advantageonlineshopping.com/#/myAccount")

        # Sign out
        self.navigation_line.sign_out_option()
        self.navigation_line.wait_for_invisibility_of_username()

        # Verify that account options not open
        self.navigation_line.click_account_icon()
        account_option_style = self.navigation_line.account_options_small_window_style()
        self.assertEqual(account_option_style, "display: none;")

        # Login again for deletion
        self.login_page.type_username("aviel12")
        self.login_page.type_password("Aviel123")
        self.login_page.signin()

        # Delete the account
        self.navigation_line.wait_for_visibility_of_username()
        self.navigation_line.my_account_option()
        # self.account_page.click_delete_account()
        self.account_page.force_delete_account()
        print("Account Deleted")

    def tearDown(self):
        # Close the test
        #self.driver.close()
        pass

