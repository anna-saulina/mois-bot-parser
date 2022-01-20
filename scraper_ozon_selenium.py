import json
from collections import Counter
import re
import time
from decimal import Decimal
from random import randint
from time import sleep

import requests
import bs4
import nltk
from nltk.corpus import stopwords
from pprint import pprint

# from requests_html import HTMLSession
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


from services import extract_product_weight


def scrape_ozon_price():
    url = 'https://www.ozon.ru/category/kofe-9372/?page=2'

    # service = Service(executable="/usr/local/bin/geckodriver")

    # Safari,  run on Mac only
    # safari_options = SafariOptions()
    # safari_options.add_argument("--headless")
    # driver = webdriver.Safari(options=safari_options)

    # Chrome
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Firefox
    # service = Service(executable_path=GeckoDriverManager().install())
    # firefox_options = FirefoxOptions()
    # firefox_options.add_argument("--headless")
    # driver = webdriver.Firefox(service=service, options=firefox_options)

    driver.get(url)
    html = driver.page_source
    print(html)

    # sleep for two second then scroll to the bottom of the page
    time.sleep(randint(3, 4))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(randint(4, 5))  # sleep between loadings

    unit_blocks = driver.find_elements(By.CSS_SELECTOR, value='.hj1')

    # unit_blocks = soup.select('div.hj0.hj1')
    print(f'Unit block length: {len(unit_blocks)}')
    pprint(f'Unit block: {unit_blocks[0]}')

    product_list = []

    for unit in unit_blocks:
        try:
            price = unit.find_element(By.CSS_SELECTOR, value='.ui-p9.ui-q1.ui-q4').text.split()
        except NoSuchElementException:
            price = None

        try:
            title = unit.find_element(By.CSS_SELECTOR, value='.c8i.i8c.c9i.jc0.f-tsBodyL.gz9').text
        except NoSuchElementException:
            title = None

        try:
            link = unit.find_element(By.CSS_SELECTOR, value='.tile-hover-target.gz9').get_attribute('href')
        except NoSuchElementException:
            link = None

        weight_measure = extract_product_weight(title)

        unit_dict = {
            'title': title,
            'price': float(round(Decimal(price[0]), 2)) if price else None,
            'currency': price[1] if price else None,
            'link': link,
            'weight': weight_measure[0],
            'measure': weight_measure[1]
        }
        product_list.append(unit_dict)

    pprint(product_list)

    driver.quit()

    json_string = json.dumps(product_list, sort_keys=True, indent=4, ensure_ascii=False)
    print(json_string)

    if len(product_list) > 0:
        with open('./ozon_price.json', 'w', encoding='utf-8') as outfile:
            json.dump(product_list, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    return product_list


if __name__ == '__main__':
    result = scrape_ozon_price()



