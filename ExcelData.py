from os import path
from openpyxl import load_workbook

# DATA (Excel) location
Data_folder = path.join(path.dirname(__file__), 'Data')
AOS_data_path = path.join(path.join(Data_folder, 'AOS_DATA.xlsx'))

workbook = load_workbook(AOS_data_path)

sheet = workbook.active


def return_info(title_column, info_column):
    d = {}
    index = 0
    for title in title_column:
        d[title.value] = info_column[index].value
        index += 1
    return d


class ExcelData:
    def __init__(self):
        self.test_column = {1: "C", 2: "D", 3: "E", 4: "F", 5: "G", 6: "H", 7: "I", 8: "J", 9: "K", 10: "L"}

    def product1(self, test_num):
        title_column = sheet["B"][1:5]
        info_column = sheet[self.test_column[test_num]][1:5]

        return return_info(title_column, info_column)

    def product2(self, test_num):
        title_column = sheet["B"][5:9]
        info_column = sheet[self.test_column[test_num]][5:9]

        return return_info(title_column, info_column)

    def product3(self, test_num):
        title_column = sheet["B"][9:13]
        info_column = sheet[self.test_column[test_num]][9:13]

        return return_info(title_column, info_column)

    def existing_account(self, test_num):
        title_column = sheet["B"][13:15]
        info_column = sheet[self.test_column[test_num]][13:15]

        return return_info(title_column, info_column)

    def new_account(self, test_num):
        title_column = sheet["B"][15:17]
        info_column = sheet[self.test_column[test_num]][15:17]
        return return_info(title_column, info_column)

    def safe_pay(self, test_num):
        title_column = sheet["B"][27:29]
        info_column = sheet[self.test_column[test_num]][27:29]
        return return_info(title_column, info_column)

    def master_card(self, test_num):
        title_column = sheet["B"][29:34]
        info_column = sheet[self.test_column[test_num]][29:34]
        return return_info(title_column, info_column)

    def results(self, test_num):

        # Have a bug init
        title_column = sheet["B"][34]
        info_column = sheet[self.test_column[test_num]][34]
        return return_info(title_column, info_column)


data = ExcelData()

print(data.product1(1))
print(data.product2(2))
print(data.product3(3))
print(data.safe_pay(4))
print(data.master_card(5))
