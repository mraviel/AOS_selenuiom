from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrdersPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def order_numbers(self):
        """ Return all order numbers : list """

        table = self.driver.find_element(By.CSS_SELECTOR, "#myAccountContainer > div > table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        order_numbers = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 3:
                order_numbers.append(cells[0].text)
        return order_numbers

    def all_orders(self):
        """ Return all orders """
        table = self.driver.find_element(By.CSS_SELECTOR, "#myAccountContainer > div > table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # d = {"order number": [], [], []}

        d = {}
        a = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 3:

                a.clear()
                order_number = cells[0].text
                product_details = []
                for cell in cells[3:6]:
                    product_details.append(cell.text)

                d[order_number] = [product_details]
                a.append(order_number)
            else:
                total_cells = []
                for cell in cells:
                    total_cells.append(cell.text)
                try:
                    d[a[0]].append(total_cells)
                except:
                    print("____")
                    print(a)
                    print(d)

        return d

            # first_there = []
            # a = []
            # v = []
            # count = 0
            # for cell in cells:
            #         first_there.append(cell)
            #         count += 1
            #         if count > 2:
            #             a.append(cell)
            #     else:
            #         v.append(cell)
            # first_there.append(a)
            # l.append()


    """
    
    all_orders = []
        a = []
        order_details = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 3:
                all_orders.append(order_details)
                order_details.clear()
                order_details.append(cells[:3].append(cells[6]))
                product_details = cells[3:6]
            else:
                product_details = cells

            order_details.append(product_details)
            
    """

