from selenium import webdriver
import csv
import requests
import time

DRIVER_PATH = '/Users/kimberleyellars/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('http://quotes.toscrape.com/')

log_in_square = driver.find_element_by_class_name("col-md-4")
log_in = log_in_square.find_element_by_tag_name("a")
log_in.click()

inputs = driver.find_elements_by_tag_name("input")
username = inputs[1]
password = inputs[2]

username.send_keys("username")
password.send_keys("password")

driver.quit()
