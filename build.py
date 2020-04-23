import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import regex as re
import csv
from datetime import date
import os

driver = webdriver.Safari()
driver.get('https://ri-department-of-health-covid-19-data-rihealth.hub.arcgis.com')

read_number = lambda title: int(driver.find_element_by_css_selector("[title='" + title + "'] ~ .text-left > .ss-value").text.replace(',',''))

dict_key_values = {}
try:
    WebDriverWait(driver, 10).until(lambda x: driver.find_element_by_css_selector("[title='Covid-19 Negative '] ~ .text-left > .ss-value:not(:empty)"))
    dict_key_values['total_negative'] = read_number("Covid-19 Negative ")
    dict_key_values['total_fatalities'] = read_number("COVID-19 Fatalities")
    dict_key_values['total_positive'] = read_number("Total COVID-19 Positive")
    dict_key_values['new_cases'] = read_number("Newly Reported Positive Tests ")

    dict_key_values['hospitalized'] = read_number(" Currently Hospitalized")
    dict_key_values['icu'] = read_number("Currently in ICU")
    dict_key_values['vent'] = read_number("Currently on Vent")
    # dict_key_values['discharged'] = read_number("visual-container-modern:nth-child(11) .cardItemContainer:nth-child(4) > .caption")

    filename = 'archive/' + str(date.today()) + '.csv'
    with open(filename, 'w') as f:
        for key in dict_key_values.keys():
            f.write("%s,%s\n"%(key,dict_key_values[key]))

    print(os.system('cp -f ' + filename + ' latest.csv'))
except Exception as e:
    print(e)
finally:
    driver.quit()
