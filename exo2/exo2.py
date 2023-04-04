import requests
from bs4 import BeautifulSoup
import pandas as pd

url= ""
s = requests.Session()
r = s.get(url)

soup=BeautifulSoup(r.text, "html.parser")
