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

root = "#pvExplorationHost > div > div > exploration > div > explore-canvas-modern > div > div.canvasFlexBox > div > div.displayArea.disableAnimations.fitToPage > div.visualContainerHost > visual-container-repeat"
svg = "transform > div > div.vcBody.themableBackgroundColor.themableBorderColorSolid > visual-modern > div > svg"
dict_key_values['total_tested'] = WebDriverWait(driver, 3).until(lambda x: read_number(root + " > visual-container-modern:nth-child(1) > " + svg))
dict_key_values['total_negative'] = read_number(root + " > visual-container-modern:nth-child(10) > " + svg + " > g:nth-child(1) > text")
dict_key_values['new_positive'] = read_number(root + " > visual-container-modern:nth-child(8) > " + svg + " > g:nth-child(1) > text > tspan")
dict_key_values['total_fatalities'] = read_number(root + " > visual-container-modern:nth-child(7) > " + svg + " > g:nth-child(1) > text")
dict_key_values['new_fatalities'] = read_number(root + " > visual-container-modern:nth-child(6) > " + svg + " > g:nth-child(1) > text")
dict_key_values['total_positive'] = read_number(root + " > visual-container-modern:nth-child(9) > " + svg)

filename = 'archive/' + str(date.today()) + '.csv'
with open(filename, 'w') as f:
    for key in dict_key_values.keys():
        f.write("%s,%s\n"%(key,dict_key_values[key]))

print(os.system('cp -f ' + filename + ' latest.csv'))
driver.quit()
