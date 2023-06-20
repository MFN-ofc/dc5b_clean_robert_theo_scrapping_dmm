import pandas as pd
data = pd.read_csv("e.csv")

data[['Genre1','Genre2','Genre3']] = data.Genre.str.split(",",expand=True)

data.to_csv('z.csv')