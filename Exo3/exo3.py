import requests
from bs4 import BeautifulSoup
import pandas as pd

filtered_data = []
id = 0
page_num = 1
    #parametre pagenum pour changer de page une fois la fin du form atteint 🥶
url = f"http://annuairesante.ameli.fr/professionnels-de-sante/recherche/liste-resultats-page-{page_num}-par_page-20-tri-distance_asc.html"
s = requests.Session()
cookies = {
'AmeliDirectPersist': '1651564855.42527.0000',
'TS01b76c1f': '0139dce0d2f5ddc4f58fd086d8c25f7d0b25e03bf3fa12c4d3454282fe498878b9c657820888c80086e46f70a0dd6b722164c98d08',
'TS019773cb': '0139dce0d202b77b2b3983dbf67b2fe5f1dfdcad7c2b2c5808c78f4b34d5709b6ec0d6f607a5550114fe2bed456a4dac064de531f1',
'infosoins': 'q9u4tgdtrf9s5lmfmbjga5qb73',
}
# Boucle pour parcourir les pages
for i in range(1, 34):
    url = f'http://annuairesante.ameli.fr/professionnels-de-sante/recherche/liste-resultats-page-{i}-par_page-20-tri-distance_asc.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://annuairesante.ameli.fr/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    r = s.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.text, "html.parser")
    #la soupe 🥣
    praticiens = soup.find_all('div', {'class': 'item-professionnel-inner'})
    print(r)
    for praticien in praticiens:
        
        if  praticien.find('h2', {'class': 'ignore-css'}) is not None:
            name = praticien.find('h2', {'class': 'ignore-css'}).text.strip()
        else:
            div_nom=praticien.find('div', {'class': 'nom_pictos centre-sante'})
            name = div_nom.find('h2').text.strip()
        tel_div = praticien.find('div', {'class': 'tel'})
        if tel_div is not None:
            tel = tel_div.text.strip()
        else:
            tel = None
        adresse = praticien.find('div', {'class': 'adresse'}).text.strip()
        print(f"Pays : {name},  Population : {tel}, Taille : {adresse}\n")
        # Ajouter les données au tableau
        filtered_data.append([id, name, tel, adresse])
        id += 1
    print(page_num)
    page_num += 1

# Création d'un dataframe pour créer le fichier csv
df = pd.DataFrame(filtered_data, columns=['ID', 'Nom du praticien', 'Téléphone', 'Adresse'])
#Enregistrement du DF dans le fameux fichier csv 
df.to_csv('/Users/theorobert/Desktop/dc5b_clean_robert_theo_scrapping_dmm/exo3/result.csv', index=False)
#petit message en mode c'est bon c'est fini
print("Fichier CSV a été créé avec douceur")
