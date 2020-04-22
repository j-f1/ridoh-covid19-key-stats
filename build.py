import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import regex as re
import csv
from datetime import date
import os

driver = webdriver.Safari()
driver.get('https://app.powerbigov.us/view?r=eyJrIjoiMDQ5YzRhNzktZTRiNS00YjFkLWFiMGItYzliOWQ2MDNmODExIiwidCI6IjJkMGYxZGI2LWRkNTktNDc3Mi04NjVmLTE5MTQxNzVkMDdjMiJ9')

read_number = lambda selector: int(driver.find_element_by_css_selector(selector).text.replace(',',''))

dict_key_values = {}
try:
    WebDriverWait(driver, 10).until(lambda x: driver.find_element_by_css_selector("visual-container-modern:nth-child(10) title"))
    dict_key_values['total_negative'] = read_number("visual-container-modern:nth-child(10) title")
    dict_key_values['total_fatalities'] = read_number("visual-container-modern:nth-child(7) title")
    dict_key_values['total_positive'] = read_number("visual-container-modern:nth-child(9) title")
    dict_key_values['new_cases'] = read_number("visual-container-modern:nth-child(8) title")

    WebDriverWait(driver, 10).until(lambda x: driver.find_element_by_css_selector("visual-container-modern:nth-child(11) .cardItemContainer:nth-child(1) > .caption"))

    dict_key_values['hospitalized'] = read_number("visual-container-modern:nth-child(11) .cardItemContainer:nth-child(1) > .caption")
    dict_key_values['icu'] = read_number("visual-container-modern:nth-child(11) .cardItemContainer:nth-child(2) > .caption")
    dict_key_values['vent'] = read_number("visual-container-modern:nth-child(11) .cardItemContainer:nth-child(3) > .caption")
    dict_key_values['discharged'] = read_number("visual-container-modern:nth-child(11) .cardItemContainer:nth-child(4) > .caption")

    filename = 'archive/' + str(date.today()) + '.csv'
    with open(filename, 'w') as f:
        for key in dict_key_values.keys():
            f.write("%s,%s\n"%(key,dict_key_values[key]))

    print(os.system('cp -f ' + filename + ' latest.csv'))
finally:
    driver.quit()
