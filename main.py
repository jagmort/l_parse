from bs4 import BeautifulSoup
from time import sleep

import csv
import lxml
import random
import requests


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/120.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'}

url = 'https://neolex.iling.spb.ru/search'
response = requests.get(url, HEADERS)
sleep(random.randrange(2, 5))

soup = BeautifulSoup(response.text, 'lxml')

# test = {}

tables = soup.find_all('div', {'class': 'entry-grid-row views-row'})
for table in tables:
    name = table.find('span', {'class': 'field field--name-title field--type-string field--label-hidden'}).text
    links = [l.text for l in table.find('div', {'class': 'sense-references'}).find_all('span', {'class': 'field field--name-title field--type-string field--label-hidden'})]
    themes = table.find('span', {'class': 'border badge'}).text
    print(name, links, themes)

