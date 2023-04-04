import requests
from bs4 import BeautifulSoup
import pandas as pd

url= "https://www.scrapethissite.com/pages/simple/"
s = requests.Session()
r = s.get(url)

soup=BeautifulSoup(r.text, "html.parser")
countries = soup.find_all('div', {'class': 'col-md-4 country'})

for card in countries:
    city = card.find('h3', {'class': 'country-name'}).text.strip()
    capital = card.find('span', {'class': 'country-capital'}).text.strip()
    population = card.find('span', {'class': 'country-population'}).text.strip()
    area = card.find('span', {'class': 'country-area'}).text.strip()
    print(f"Pays : {city}, Capitale : {capital}, Population : {population}, Taille : {area}\n")