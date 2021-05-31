#!/usr/bin/python
# -*- coding: ascii -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.python.org")

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdTgQB83_s8awG9_k068kWFLyd2vMAtRQionqYrdSJYw5km4A/viewform")
time.sleep(2)

print(driver.title)

last = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys("Pepe")

inputradio = driver.find_element_by_xpath('//*[@id="i9"]/div[3]/div')
inputradio.click()

Submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()

# get_confirmation_div_text = driver.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
# print(get_confirmation_div_text.text)
# if ((get_confirmation_div_text.text) == "Se registro tu respuesta."):
#     print("Test Was Successful")
# else:
#     print("Test Was Not Successful")