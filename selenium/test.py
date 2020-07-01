
from selenium import webdriver
import xlsxwriter
import pandas as pd
path = webdriver.Chrome()

path.get("https://covid.hespress.com/")

workbook = xlsxwriter.Workbook('./example.xlsx')
worksheet = workbook.add_worksheet()
x = 1
while x <= 12:
    worksheet.write(f'{chr(64+x)}1', path.find_element_by_xpath(f"""/html/body/div[1]/div[1]/div[13]/div/div[2]/table/tbody/tr[{x}]/th/a""").text)
    worksheet.write(f'{chr(64+x)}2', path.find_element_by_xpath(f"""/html/body/div[1]/div[1]/div[13]/div/div[2]/table/tbody/tr[{x}]/td[1]""").text)
    worksheet.write(f'{chr(64+x)}3', path.find_element_by_xpath(f"""/html/body/div[1]/div[1]/div[13]/div/div[2]/table/tbody/tr[{x}]/td[2]""").text)
    x +=1
workbook.close()
# workbook.save()