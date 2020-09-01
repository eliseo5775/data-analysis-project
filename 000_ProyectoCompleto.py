# Descarga de data de dataset de twetts http://galileoguzman.com/data/covid19_tweets.csv
import requests

#df_web = requests.get('http://galileoguzman.com/data/covid19_tweets.csv')
#print(df_web.status_code)

# Ejecuta una función que calcule cuantos días transcurridos han pasado hasta
# el día que se ejecute, desde la primera vez que un usuario publicó un tweet
# acerca del CoronaVirus
import pandas as pd

FILENAME = 'Dataset/covid19_tweeets.csv'

df = pd.read_csv(FILENAME)

