from time import sleep
from random import randint
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd

# tạo dataframe
df = pd.DataFrame(columns=["Name", "Classify", "Content", "TimeStamp"])

url = "https://shopee.vn/G%E1%BB%8Dng-k%C3%ADnh-c%E1%BA%ADn-vu%C3%B4ng-cao-c%C3%A2%CC%81p-1220-%E2%80%93-Ti%C3%AA%CC%A3m-ki%CC%81nh-Candy-i.203796246.5616887415"
browser = webdriver.Chrome(executable_path="E:/Python project/Crawl_data/chromedriver.exe")
browser.get(url)
sleep(randint(3,5))

# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # scroll to last screen
# This  will scroll page 400 pixel vertical
browser.execute_script("window.scrollTo(0,2700)")
sleep(randint(5,7))

page = 0
while page < 5:
    page_source = BeautifulSoup(browser.page_source, 'html.parser') # in ra html
    product_rating_list = page_source.find_all('div', class_ = 'shopee-product-rating__main')
    for product_rating in product_rating_list:
        try:
            name = product_rating.find('a', class_ = 'shopee-product-rating__author-name').get_text().strip()
            print("Name: " + name)

            classify = product_rating.find('span', class_ = 'shopee-product-rating__variation').get_text().strip()
            print(classify)

            content = product_rating.find('div', class_ = 'shopee-product-rating__content').get_text().strip()
            print("Nội dung: " + content)

            timestamp = product_rating.find('div', class_ = 'shopee-product-rating__time').get_text().strip()
            print("Thời gian: " + timestamp)
            print("\n")
        except:
            pass

        df = df.append({"Name": name, "Classify": classify, "Content": content , "TimeStamp": timestamp},ignore_index=True)

    button_next = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[2]/button[8]')
    button_next.click()
    sleep(randint(3,5))

    page += 1

df.to_csv("shope_rating.csv", sep='\t', encoding='utf-8', index=False)


