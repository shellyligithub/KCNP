# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:11:38 2019

@author: igloo
"""

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Get user's iteneray
hotelList = ['All Properties','Wuksachi Lodage','John Muir Lodge', \
            'Grant Grove Cabins', 'Cedar Grove Lodage', 'Bearpaw High Sierra Camp']

print('Where do you like to stay?')
print('1 All Properties')
print('2 Wuksachi Lodage')
print('3 John Muir Lodge')
print('4 Grant Grove Cabins')
print('5 Cedar Grove Lodage')
print('6 Bearpaw High Sierra Camp')

#hotelID = input('Enter the number for your selection:')
#hotel = hotelList[int(hotelID)-1]
hotel = hotelList[0]
print('your hotel selection is: ' + hotel)
monthYear = 'NOVEMBER 2019'
dayStart = '28'
dayEnd = '29'
kidNum = 2
adultNum = 3


# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://www.visitsequoia.com/lodging')

# Locate hotel
selectHotel = Select(driver.find_element_by_id("checkRatesLocation"))
selectHotel.select_by_visible_text(hotel)

# Select arrival and departual date
datepicker = driver.find_element_by_id('checkRatesTravelDates')
datepicker.click()
time.sleep(1)
# Selet month and year
emy = driver.find_elements_by_xpath("//*[@id='main']/div[2]/div/section/div[2]/div/div[2]/table/thead/tr/th[@class='month-name']")
while(emy[0].text != monthYear):
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div[2]/div/div[2]/table[2]/thead/tr[1]/td[2]/span").click()
# Selet day
ed1 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div[2]/div/div[2]/table[1]/tbody")
ed2 = ed1.find_elements_by_tag_name('tr')
time.sleep(1)
for rows in ed2:
    columns = rows.find_elements_by_tag_name('td')
    for col in columns:
        if(col.text == dayStart):
            col.find_element_by_tag_name('div').click()
        if(col.text == dayEnd):
            end = col.find_element_by_tag_name('div').click()

# Check availability
window_before = driver.window_handles[0]
checkAvailabilityButton = driver.find_element_by_xpath("//*[@id='btnCheckRatesBodyCalloutSubmit']")
time.sleep(1)
checkAvailabilityButton.click()
time.sleep(1)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

# Input adult and children number
selectAdult = Select(driver.find_element_by_xpath("//*[@id='V150_C1_QuantitiesCntrl_RoomsRepeater_ctl00_AdultsDropdown']"))
selectAdult.select_by_visible_text(str(adultNum))
selectKid = Select(driver.find_element_by_xpath("//*[@id='V150_C1_QuantitiesCntrl_RoomsRepeater_ctl00_ChildrenDropdown']"))
selectKid.select_by_visible_text(str(kidNum))

# Check availability
checkAvailabilityButton2 = driver.find_element_by_id("V150_C1_CBtn")
checkAvailabilityButton2.click()
