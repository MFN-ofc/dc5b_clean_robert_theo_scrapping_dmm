import requests
from bs4 import BeautifulSoup
import pandas as pd

filtered_data = []
id = 0
page_num = 1
while page_num <= 10:
    #parametre pagenum pour changer de page une fois la fin du form atteint 🥶
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={page_num}"
    s = requests.Session()
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    #la soupe 🥣
    teams = soup.find_all('tr', {'class': 'team'})
    for team in teams:
        name = team.find('td', {'class': 'name'}).text.strip()
        year = team.find('td', {'class': 'year'}).text.strip()
        wins = team.find('td', {'class': 'wins'}).text.strip()
        losses = team.find('td', {'class': 'losses'}).text.strip()
        ot_losses = team.find('td', {'class': 'ot-losses'}).text.strip()
        pct = team.find('td', {'class': 'pct'}).text.strip()
        gf = team.find('td', {'class': 'gf'}).text.strip()
        ga = team.find('td', {'class': 'ga'}).text.strip()
        diff = team.find('td', {'class': 'diff'}).text.strip()
        if diff > "0" and ga < "300":
            # Ajouter les données filtrées au tableau
            filtered_data.append([id, name, year, wins, losses, ot_losses, pct, gf, ga, diff])
            id += 1

    page_num += 1

# Création d'un dataframe pour créer le fichier csv
df = pd.DataFrame(filtered_data, columns=['ID', 'Nom de l equipe', 'Année de création', 'Victoires', 'Défaites', 'OT Losses', 'Pct', 'Buts Mis', 'Buts reçus', 'Diff'])
#Enregistrement du DF dans le fameux fichier csv 
df.to_csv('/Users/theorobert/Desktop/dc5b_clean_robert_theo_scrapping_dmm/exo2/result.csv', index=False)
#petit message en mode c'est bon c'est fini
print("Fichier CSV a été créé avec douceur")
