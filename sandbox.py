from selenium import webdriver
import csv
import requests
import time

time.sleep(.1)
DRIVER_PATH = '/Users/kimberleyellars/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('http://books.toscrape.com/')

with open('/Users/kimberleyellars/github/sandbox/books.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    page_ = driver.find_element_by_class_name("current").text
    pages = page_.split(" ")
    num_of_pages = int(pages[3])
    for i in range(num_of_pages):
        articles = driver.find_elements_by_class_name("product_pod")
        x=0
        for article in articles:
            links = article.find_elements_by_tag_name("a")
            name = links[1]
            price = article.find_element_by_class_name("price_color")
            csv_writer.writerow([name.text,price.text])
            time.sleep(.01)
            x+=1
            print(i,x)
        if i != 49:
            next_button = driver.find_element_by_class_name("next")
            next = next_button.find_element_by_tag_name("a")
            next.click()
driver.quit()
