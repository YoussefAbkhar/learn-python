
from selenium import webdriver

# import xlsxwriter
import pandas as pd
path = webdriver.Chrome()

path.get("https://covid.hespress.com/")
a = []

# i = 1
# j = 2
# k = 3
# x = 1
# while x < 12:
    # a.insert(i,path.find_element_by_xpath(f"""/html/body/div[1]/div[1]/div[13]/div/div[2]/table/tbody/tr[{x}]/th/a""").text)
    # a.insert(k,int(path.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[13]/div/div[2]/table/tbody/tr[{x}]/td[1]').text))
    # a.insert(j,int(path.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[13]/div/div[2]/table/tbody/tr[{x}]/td[2]').text))
    # i += 3
    # j += 3
    # k += 3
    # x += 1


# print(a)

# workbook = xlsxwriter.Workbook('./example.xlsx')
# worksheet = workbook.add_worksheet()
# x = 12
# while x < 12:
#     worksheet.write(f'A1', 'Hello world')
#     worksheet.write(f'A1', 'Hello world')
#     worksheet.write(f'A1', 'Hello world')

# workbook.close()
# writer.save()


print(int((path.find_element_by_xpath(f"""/html/body/div[1]/div[1]/div[13]/div/div[2]/table/tbody/tr[1]/td[2]""").text)))