from datetime import datetime
import random
from time import sleep

from bs4 import BeautifulSoup
import numpy as np
import requests


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/120.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}

url = 'https://neolex.iling.spb.ru/search?search_api_fulltext=&page={page}'

count = 0
page = 0

data = [['Name', 'Links', 'Themes']]

while count < 10:

    print('Page:', page)
    response = requests.get(url.format(page=page), HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    tables = soup.find_all('div', {'class': 'entry-grid-row views-row'})
    for table in tables:
        name = table.find('span', {
            'class': 'field field--name-title field--type-string field--label-hidden'}).text.strip()
        links = [l.text.strip() for l in table.find('div', {'class': 'sense-references'}).find_all(
            'span', {'class': 'field field--name-title field--type-string field--label-hidden'})]
        themes = table.find('span', {'class': 'border badge'}).text.strip()
        print(name, links, themes)

        data.append([name, ','.join(links), themes])
        count += 1

    sleep(random.randrange(2, 5))
    page += 1

filename = datetime.now().strftime('%Y%m%d_%H%M%S.csv')
np.savetxt(filename,
           data,
           delimiter=";",
           fmt='%s')
