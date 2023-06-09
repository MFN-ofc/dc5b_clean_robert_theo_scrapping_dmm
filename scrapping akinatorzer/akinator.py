import pandas as pd

def load_movies(csv_file):
    # Charger le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(csv_file)
    return df

def ask_question(df, question, column):
    # Poser une question à l'utilisateur et filtrer le DataFrame en fonction de la réponse
    answer = input(question + " (oui/non) ")
    if answer.lower() == "oui":
        df = df[df[column].str.contains(answer, na=False)]
    elif answer.lower() == "non":
        df = df[~df[column].str.contains(answer, na=False)]
    return df

def main():
    # Charger les films à partir du fichier CSV
    df = load_movies('/Users/theorobert/Desktop/dc5b_clean_robert_theo_scrapping_dmm/scrapping akinatorzer/akinator.py')

    # Poser une série de questions pour affiner la recherche
    df = ask_question(df, "Préférez-vous un film d'action ?", "Genre")
    df = ask_question(df, "Préférez-vous un film d'aventure ?", "Genre")
    df = ask_question(df, "Préférez-vous un film sorti avant 1980 ?", "Année de sortie")
    df = ask_question(df, "Préférez-vous un film sorti après 2000 ?", "Année de sortie")
    df = ask_question(df, "Préférez-vous un film avec une note supérieure à 8 ?", "Note")
    df = ask_question(df, "Préférez-vous un film avec une note inférieure à 8 ?", "Note")
    df = ask_question(df, "Préférez-vous un film d'une durée supérieure à 2 heures ?", "Durée")

    # Si plus d'un film correspond aux critères, poser des questions supplémentaires jusqu'à ce qu'un seul film reste
    while len(df) > 1:
        df = ask_question(df, "Préférez-vous un film avec plus de 1 million de votes ?", "Nombre de votant")

    # Afficher le film qui correspond aux critères
    if not df.empty:
        print("\nLe film qui correspond à vos critères est :\n")
        print(df)
    else:
        print("\nDésolé, aucun film ne correspond à vos critères.\n")

if __name__ == "__main__":
    main()
