from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from os import path
from ExcelData import ExcelData

from Selenium_Classes.HomePage import HomePage
from Selenium_Classes.CategoryPage import Category_page
from Selenium_Classes.ProductPage import Product_page
from Selenium_Classes.NavigationLine import Navigation_line
from Selenium_Classes.SignupPage import SignupPage
from Selenium_Classes.LoginPage import LoginPage
from Selenium_Classes.AccountPage import AccountPage
from Selenium_Classes.ShoppingCart import ShoppingCart
from Selenium_Classes.OrderPayment import OrderPayment
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

        # Excel data
        self.excel = ExcelData()

        # Pages
        self.home_page = HomePage(self.driver)
        self.category_page = Category_page(self.driver)
        self.product_page = Product_page(self.driver)
        self.navigation_line = Navigation_line(self.driver)
        self.signup_page = SignupPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)
        self.order_payment_page = OrderPayment(self.driver)
        self.order_page = OrdersPage(self.driver)

        # Test number and pass
        self.test_pass = False
        self.test_num = 0

    def test_num1(self):
        """ Test after adding products to cart, all quantities are right """
        self.test_num = 1

        products_info = [self.excel.product1(1), self.excel.product2(1)]

        quantity = 0
        for product in products_info:
            self.home_page.open_category(product['category'])
            self.category_page.choose_product_by_id(product['productID'])
            self.product_page.choose_Quantity(product['quantity'])
            quantity += int(self.product_page.get_product_quantity())
            self.product_page.click_on_att_to_cart()
            self.navigation_line.click_logo_icon()

        self.assertEqual(int(self.navigation_line.quantity_from_cart()), quantity)

        # Test Pass
        self.test_pass = True

    def test_num2(self):
        """ Test that shopping cart small window to have all correct products that the user added
            matching: product name, color, quantity and price """

        self.test_num = 2

        # All relevant info for test
        excel_info = [self.excel.product1(2), self.excel.product2(2), self.excel.product3(2)]

        products_info = []  # Gather products info form product page

        # Add 3 products to cart
        for product in excel_info:
            self.home_page.open_category(product['category'])
            self.category_page.choose_product_by_id(product['productID'])
            self.product_page.choose_Quantity(product['quantity'])
            products_info.append(self.product_page.get_product_info())  # All info about product
            self.product_page.click_on_att_to_cart()
            self.navigation_line.click_logo_icon()

        # Gather all products from shopping cart small window
        products_in_cart_window = self.navigation_line.cart_small_window_products()
        products_in_cart_window.reverse()

        print(f"cart window: {products_in_cart_window}")
        print(f"product_info: {products_info}")

        # Is name, quantity, color and price expectation equal to products_in_cart_window?

        # Test product name (part name) in full name
        index = 0
        for product in products_in_cart_window:
            self.assertIn(product[0], products_info[index][0])
            print(f"{product[0]} in '{products_info[index][0]}'")
            index += 1

        # Test quantity
        index = 0
        for product in products_in_cart_window:
            self.assertEqual(int(products_info[index][1]), int(product[1]))
            print(f"{products_info[index][1]} == {product[1]}")
            index += 1

        # Test color
        index = 0
        for product in products_in_cart_window:
            self.assertEqual(products_info[index][2], product[2])
            print(f"{products_info[index][2]} == {product[2]}")
            index += 1

        # Test total price
        index = 0
        for product in products_in_cart_window:
            price = products_info[index][3][1:].replace(',', '')  # if there a ',' remove it
            quantity = products_info[index][1]
            total_price = float(price) * float(quantity)  # price * quantity

            total_price_shopping_cart = product[3][1:].replace(',', '')  # if there a ',' remove it
            self.assertEqual(total_price, float(total_price_shopping_cart))
            print(f"{total_price}$ == {product[3]}")
            index += 1

        # Test Pass
        self.test_pass = True

    def test_num3(self):
        """ Test after adding to cart two products and delete one of them, the product deleted. """

        self.test_num = 3

        products_info = [self.excel.product1(3), self.excel.product2(3)]

        names_of_products = []
        for product in products_info:
            self.home_page.open_category(product['category'])
            self.category_page.choose_product_by_id(product['productID'])
            self.product_page.choose_Quantity(product['quantity'])
            self.product_page.click_on_att_to_cart()
            names_of_products.append(self.product_page.get_product_name())
            self.navigation_line.click_logo_icon()

        self.navigation_line.remove_product_from_cart_icon(1)

        # Test that part of name (first 25 letters) in products names form cart small window
        self.assertNotIn(names_of_products[0][:25], self.navigation_line.cart_small_window_products_names())

        # Test Pass
        self.test_pass = True

    def test4(self):
        """ Test after adding to cart one product navigate to cart page """
        self.test_num = 4

        # All relevant info for test
        product = self.excel.product1(4)

        # Add one product to shopping cart
        self.home_page.open_category(product['category'])
        self.category_page.choose_product_by_id(product['productID'])
        self.product_page.choose_Quantity(product['quantity'])
        self.product_page.click_on_att_to_cart()

        # Check current location, shopping cart
        self.navigation_line.click_cart_icon()
        current_page_text = self.shopping_cart_page.logo_shopping_cart()
        self.assertEqual("SHOPPING CART", current_page_text)

        # Test Pass
        self.test_pass = True

    def test_num5(self):
        """ Test after adding to cart 3 products the final price result """
        self.test_num = 5

        products_info = [self.excel.product1(5), self.excel.product2(5), self.excel.product3(5)]

        priceofproducts = []
        for product in products_info:
            self.home_page.open_category(product['category'])
            self.category_page.choose_product_by_id(product['productID'])
            self.product_page.choose_Quantity(product['quantity'])
            x = self.product_page.get_product_price()
            x1 = x[1:]
            x1 = x1.replace(',', '')
            priceofproducts += [float(x1) * float(self.product_page.get_product_quantity())]
            print(self.product_page.get_product_info())
            self.product_page.click_on_att_to_cart()
            self.navigation_line.click_logo_icon()

        w = self.shopping_cart_page.final_price_from_shoppingcart()
        w = w.replace(',', '')
        self.assertIn(str(sum(priceofproducts)), w)
        print(self.navigation_line.final_price_from_cart_icon())
        print(sum(priceofproducts))

        # Test Pass
        self.test_pass = True

    def test6(self):
        """ Test that cart page update after editing two products from cart page """
        self.test_num = 6

        # All relevant info for test
        excel_info = [self.excel.product1(6), self.excel.product2(6)]

        # Add 2 products to cart
        for product in excel_info:
            self.home_page.open_category(product['category'])
            self.category_page.choose_product_by_id(product['productID'])
            self.product_page.choose_Quantity(product['quantity'])
            self.product_page.click_on_att_to_cart()
            self.navigation_line.click_logo_icon()

        # change products quantity
        quantity = [3, 4]
        index = 0
        for i in range(2):
            self.navigation_line.click_cart_icon()
            self.shopping_cart_page.edit_product_by_index(index)
            self.product_page.choose_Quantity(quantity[index])
            self.product_page.click_on_att_to_cart()
            index += 1

        # Get all shopping cart items
        self.navigation_line.click_cart_icon()
        cart_after_change = self.shopping_cart_page.all_shopping_cart_items()
        print(cart_after_change)

        # Check if quantity of first product change to 3
        self.assertEqual(cart_after_change[0][1], '3')

        # Check if quantity of second product change to 4
        self.assertEqual(cart_after_change[1][1], '4')

        # Test Pass
        self.test_pass = True

    def test_num7(self):
        """ Test going back from product page to category page and after that to home page """
        self.test_num = 7

        product_info = self.excel.product1(7)

        self.home_page.open_category(product_info['category'])
        self.category_page.choose_product_by_id(product_info['productID'])
        self.product_page.choose_Quantity(product_info['quantity'])
        self.product_page.click_on_att_to_cart()
        self.driver.back()
        self.assertEqual('TABLETS', self.category_page.page_name())
        self.driver.back()
        self.assertEqual('SPECIAL OFFER', self.home_page.return_SPACIAL_OFFER())

        # Test Pass
        self.test_pass = True

    def test_num8(self):
        """ Test making an order with safe-pay,
            test perches complete, cart is empty and order in order page """
        self.test_num = 8

        # All relevant info for test
        excel_info_products = [self.excel.product1(8), self.excel.product2(8)]  # [{} , {}]
        signup = self.excel.new_account(8)
        safe_pay = self.excel.safe_pay(8)

        # Add to cart few products
        for product in excel_info_products:
            self.home_page.open_category(product['category'])
            self.category_page.choose_product_by_id(product['productID'])
            self.product_page.choose_Quantity(product['quantity'])
            self.product_page.click_on_att_to_cart()
            self.navigation_line.click_logo_icon()

        # Checkout
        self.navigation_line.click_cart_icon()
        self.shopping_cart_page.click_checkout()

        self.order_payment_page.click_registration()

        # Fill info
        self.signup_page.type_username(signup['username'])
        self.signup_page.type_email(signup['email'])
        self.signup_page.type_password(signup['password'])
        self.signup_page.type_confirm_password(signup['confirm password'])
        self.signup_page.type_first_name(signup['first name'])
        self.signup_page.type_last_name(signup['last name'])
        self.signup_page.type_phone_number(signup['phone number'])
        self.signup_page.type_country(signup['country'])
        self.signup_page.type_city(signup['city'])
        self.signup_page.type_address(signup['address'])
        self.signup_page.type_state_region(signup['stats region'])
        self.signup_page.type_postal_code(signup['postal code'])
        self.signup_page.click_i_agree()
        self.signup_page.click_register()

        self.order_payment_page.next_click()
        self.order_payment_page.choose_payment_method("SafePay")
        self.order_payment_page.type_safe_pay_username(safe_pay['username'])
        self.order_payment_page.type_safe_pay_password(safe_pay['password'])
        self.order_payment_page.safe_pay_pay_now_click()

        # verify the reservation done
        thank_you_massage = self.order_payment_page.thank_for_order()
        order_number = self.order_payment_page.order_number()
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

        # Test Pass
        self.test_pass = True

    def test9(self):
        """ Test making an order with Credit-Card,
                   test perches complete, cart is empty and order in order page """
        self.test_num = 9

        # All relevant info for test
        excel_info_products = [self.excel.product1(9), self.excel.product2(9)]  # [{} , {}]
        signup = self.excel.new_account(9)
        login = self.excel.existing_account(9)
        master_card = self.excel.master_card(9)

        # Navigate to register page
        self.navigation_line.click_account_icon()
        self.login_page.click_new_account()

        # Fill info register
        self.signup_page.type_username(signup['username'])
        self.signup_page.type_email(signup['email'])
        self.signup_page.type_password(signup['password'])
        self.signup_page.type_confirm_password(signup['confirm password'])
        self.signup_page.type_first_name(signup['first name'])
        self.signup_page.type_last_name(signup['last name'])
        self.signup_page.type_phone_number(signup['phone number'])
        self.signup_page.type_country(signup['country'])
        self.signup_page.type_city(signup['city'])
        self.signup_page.type_address(signup['address'])
        self.signup_page.type_state_region(signup['stats region'])
        self.signup_page.type_postal_code(signup['postal code'])
        self.signup_page.click_i_agree()
        self.signup_page.click_register()

        self.navigation_line.wait_for_visibility_of_username()
        self.navigation_line.sign_out_option()
        print("logout good")

        self.navigation_line.click_logo_icon()
        # Add to cart few products
        for product in excel_info_products:
            self.home_page.open_category(product['category'])
            self.category_page.choose_product_by_id(product['productID'])
            self.product_page.choose_Quantity(product['quantity'])
            self.product_page.click_on_att_to_cart()
            self.navigation_line.click_logo_icon()

        # Checkout
        self.navigation_line.click_cart_icon()
        self.shopping_cart_page.click_checkout()
        print("checkout good")

        print("start login")
        # Login
        self.order_payment_page.type_username(login['username'])
        self.order_payment_page.type_password(login['password'])
        self.order_payment_page.click_login()

        print("done login")

        self.order_payment_page.next_click()
        self.order_payment_page.choose_payment_method("MasterCredit")
        self.order_payment_page.type_credit_card_number(master_card['card number'])
        self.order_payment_page.type_credit_cvv_number(master_card['cvv'])
        self.order_payment_page.credit_expiration_date_mm(master_card['mm'])
        self.order_payment_page.credit_expiration_date_yy(master_card['yy'])
        self.order_payment_page.type_credit_cardholder(master_card['card holder'])
        self.order_payment_page.credit_pay_now_click()

        order_number = self.order_payment_page.order_number()

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

        # Test Pass
        self.test_pass = True

    def test_num10(self):
        """ Test login and logout successfully  """
        self.test_num = 10

        # All relevant info for test
        signup = self.excel.new_account(10)
        login = self.excel.existing_account(10)

        # Navigate to register page
        self.navigation_line.click_account_icon()
        self.login_page.click_new_account()

        # Fill info
        self.signup_page.type_username(signup['username'])
        self.signup_page.type_email(signup['email'])
        self.signup_page.type_password(signup['password'])
        self.signup_page.type_confirm_password(signup['confirm password'])
        self.signup_page.type_first_name(signup['first name'])
        self.signup_page.type_last_name(signup['last name'])
        self.signup_page.type_phone_number(signup['phone number'])
        self.signup_page.type_country(signup['country'])
        self.signup_page.type_city(signup['city'])
        self.signup_page.type_address(signup['address'])
        self.signup_page.type_state_region(signup['stats region'])
        self.signup_page.type_postal_code(signup['postal code'])
        self.signup_page.click_i_agree()
        self.signup_page.click_register()

        # Login
        self.navigation_line.click_account_icon()
        self.login_page.type_username(login['username'])
        self.login_page.type_password(login['password'])
        self.login_page.signin()

        # Is username beside account icon ?
        located_username = self.navigation_line.username_appearance()
        self.assertEqual(login['username'], located_username)

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
        self.assertEqual(account_option_style, "display: none;")  # none = close, block = open

        # Login again for deletion
        self.login_page.type_username(login['username'])
        self.login_page.type_password(login['password'])
        self.login_page.signin()

        # Delete the account
        self.navigation_line.wait_for_visibility_of_username()
        self.navigation_line.my_account_option()
        # self.account_page.click_delete_account()
        self.account_page.force_delete_account()
        print("Account Deleted")

        # Test Pass
        self.test_pass = True

    def tearDown(self):

        # Write to excel the test result
        if self.test_pass:
            self.excel.pass_and_failed(self.test_num, "V")
        else:
            self.excel.pass_and_failed(self.test_num, "X")

        # Close the browser
        self.driver.close()
