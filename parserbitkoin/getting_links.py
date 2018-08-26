import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)
    return r.content


def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    links = []
    for td in tds:
        link = 'https://coinmarketcap.com' + td.find('a', class_='currency-name-container').get('href')
        links.append(link)
    return links

