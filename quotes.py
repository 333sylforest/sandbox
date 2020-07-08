from selenium import webdriver
import csv
import requests
import time

time.sleep(.1)
DRIVER_PATH = '/Users/kimberleyellars/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('http://quotes.toscrape.com/')

with open('/Users/kimberleyellars/github/sandbox/quotes.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    next_button = driver.find_element_by_class_name("next")
    for i in range(10):
        quote_cards = driver.find_elements_by_class_name("quote")
        for quote_card in quote_cards:
            quote = quote_card.find_element_by_class_name("text").text
            author = quote_card.find_element_by_class_name("author").text
            csv_writer.writerow([quote,author])
        if i != 9:
            next_button = driver.find_element_by_class_name("next")
            next = next_button.find_element_by_tag_name("a")
            next.click()

driver.quit()
