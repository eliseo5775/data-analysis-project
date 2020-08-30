# Descarga de data de dataset de twetts http://galileoguzman.com/data/covid19_tweets.csv
import requests

df = requests.get('http://galileoguzman.com/data/covid19_tweets.csv')
print(df.status_code)

# Ejecuta una función que calcule cuantos días transcurridos han pasado hasta
# el día que se ejecute, desde la primera vez que un usuario publicó un tweet
# acerca del CoronaVirus
import pandas as pd

