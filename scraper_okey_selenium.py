import json
import time
from random import randint

from pprint import pprint

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from services import parse_price, extract_okey_product_weight, GRAM, find_minimum_price


def scrape_ozon_price():
    url = 'https://www.okeydostavka.ru/spb/goriachie-i-kholodnye-napitki/kofe-kakao-tsikorii/kofe#facet' \
          ':-7000000000000024651104232107910771088108510721093,' \
          '-70000000000000246511052108610831086109010991081&productBeginIndex:0&orderBy:&pageView:grid&minPrice' \
          ':&maxPrice:&pageSize:& '

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
    # print(html)

    # sleep for two second then scroll to the bottom of the page
    time.sleep(randint(3, 4))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(randint(4, 5))  # sleep between loadings

    unit_blocks = driver.find_elements(By.CSS_SELECTOR, value='.product.ok-theme')

    product_list = []

    for unit in unit_blocks:
        try:
            price = unit.find_element(By.TAG_NAME, value='input').get_attribute('value').split()
            # print(price)
        except NoSuchElementException:
            price = None

        try:
            title = unit.find_element(By.TAG_NAME, value='a').get_attribute('title')
        except NoSuchElementException:
            title = None

        try:
            link = unit.find_element(By.TAG_NAME, value='a').get_attribute('href')
        except NoSuchElementException:
            link = None

        if price:
            converted_price = parse_price(price)
            if len(price) == 2:
                currency = price[1]
            if len(price) == 3:
                currency = price[2]
        else:
            converted_price = None
            currency = None

        weight_measure = extract_okey_product_weight(title)

        if weight_measure[0] and weight_measure[1]:
            if weight_measure[1] in GRAM:
                price_kg = converted_price / weight_measure[0] * 1000
            else:
                price_kg = converted_price
        else:
            price_kg = None

        unit_dict = {
            'title': title,
            'price': converted_price if converted_price else None,
            'price_kg': price_kg,
            'currency': currency if currency else None,
            'link': link,
            'weight': weight_measure[0] if weight_measure else None,
            'measure': weight_measure[1] if weight_measure else None
        }
        product_list.append(unit_dict)

    pprint(product_list)

    minimum_price_product = find_minimum_price(product_list)

    driver.quit()

    json_string = json.dumps(product_list, sort_keys=True, indent=4, ensure_ascii=False)
    print(json_string)

    if len(product_list) > 0:
        with open('./okey_price.json', 'w', encoding='utf-8') as outfile:
            json.dump(product_list, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    if minimum_price_product:
        with open('./okey_minimum_price.json', 'w', encoding='utf-8') as outfile:
            json.dump(minimum_price_product, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    return minimum_price_product


if __name__ == '__main__':
    result = scrape_ozon_price()
    print(result)
