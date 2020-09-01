# Descarga de data de dataset de twetts http://galileoguzman.com/data/covid19_tweets.csv
import requests
import pandas as pd
from datetime import date

#df_web = requests.get('http://galileoguzman.com/data/covid19_tweets.csv')
#print(df_web.status_code)

FILENAME = 'Dataset/covid19_tweets.csv'
df = pd.read_csv(FILENAME)

print(df.head())

# Ejecuta una función que calcule cuantos días transcurridos han pasado hasta
# el día que se ejecute, desde la primera vez que un usuario publicó un tweet
# acerca del CoronaVirus

def diastranscurridos(df_input001):
    current_date = date.today()
    print(current_date)
    return

diastranscurridos(df)



