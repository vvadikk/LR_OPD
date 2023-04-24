import requests
from bs4 import BeautifulSoup
import zapis
def parse():
    page = requests.get('https://www.imdb.com/chart/top/')
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    t0p = soup.findAll('td', class_='titleColumn')
    r0ting = soup.findAll('td', class_='ratingColumn imdbRating')
    top = []
    rating = []
    for i in t0p:
        top.append(i.find('a').text)
    for i in r0ting:
        rating.append(i.find('strong').text)
    zapis.vfile(top, rating)