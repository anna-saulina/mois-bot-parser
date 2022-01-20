# from collections import Counter
# import re
# from random import randint
# from time import sleep
#
# import requests
# import bs4
# import nltk
# from nltk.corpus import stopwords
# from pprint import pprint
#
# from requests_html import HTMLSession
#
#
# # def scrape():
# #     url = 'http://www.analytictech.com/mb021/mlk.htm'
# #     page = requests.get(url)
# #     page.raise_for_status()
# #
# #     soup = bs4.BeautifulSoup(page.text, 'html.parser')
# #     # print(soup.prettify())
# #
# #     p_elems = [element.text for element in soup.find_all('p')]
# #     speech = ''.join(p_elems)
# #     print(speech)
# #
# #
# # def check_price(URL, threshold_amt):
# #     headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
# #     page = requests.get(URL,headers=headers)
# #     soup = bs4.BeautifulSoup(page.content,'html.parser')
# #     title = soup.find(id="productTitle").get_text().strip()
# #     price = soup.find(id="priceblock_saleprice").get_text()[1:].strip().replace(',','')
# #     Fprice = float(price)
# #     if Fprice < threshold_amt:
# #         pass
#
#
# def scrape_price():
#     url = 'https://www.ozon.ru/brand/teatone-76883530/?page=4'
#     page = requests.get(url)
#     page.raise_for_status()
#
#     # session = HTMLSession()
#     # r = session.get(url)
#     # about = r.html.find('.hj0.hj1')
#     # print(len(about))
#
#     soup = bs4.BeautifulSoup(page.text, 'html.parser')
#     # soup = bs4.BeautifulSoup(html_page.text, 'html.parser')
#     print(soup.prettify())
#
#     # unit_blocks = [element for element in soup.find_all('div', class_='hj1')]
#     # # print(f'Unit block: {unit_blocks[0]}')
#     # print(f'Unit block length: {len(unit_blocks)}')
#     #
#     # # unit_blocks = soup.find_all(class_='hj0 hj1')
#     # # unit_blocks = soup.select('div.hj0.hj1')
#     # # print(f'Unit block length: {len(unit_blocks)}')
#     # # pprint(f'Unit block: {unit_blocks[0]}')
#     #
#     # # for i in range(3):
#     # #     price = [element.get_text().split() for element in soup.find_all('span', class_='ui-p9 ui-q1 ui-q4')]
#     # #     pprint(f'{i}: {price}')
#     # #     sleep(randint(2, 5))
#     #
#     # search_wiget = [element for element in soup.select('div.hl6')]
#     # print(f'search_wiget: {len(search_wiget)}')
#     # # pprint(f'{search_wiget}')
#     #
#     # product_list = []
#     #
#     # for unit in unit_blocks:
#     #     title = unit.find('span', class_='c8i i8c c9i jc0 f-tsBodyL gz9').get_text()
#     #     price = unit.find('span', class_='ui-p9 ui-q1 ui-q4').get_text().split()
#     #     link = unit.find('a', class_='tile-hover-target gz9').get('href')
#     #     # price_list = [price. for price in prices]
#     #     unit_dict = {
#     #         'title': title,
#     #         'price': price,
#     #         # 'currency': price[1],
#     #         'link': link
#     #     }
#     #     product_list.append(unit_dict)
#     #
#     # pprint(product_list)
#
#
# if __name__ == '__main__':
#     scrape_price()
