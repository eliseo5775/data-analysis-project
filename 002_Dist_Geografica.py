#import requirements
from datetime import date
import pandas as pd 
import matplotlib.pyplot as plt

FILENAME = 'Dataset/covid19_tweets.csv'
df = pd.read_csv(FILENAME)

#Transformas la data
df["user_name"] = df['user_name'].astype('string')
df["user_location"] = df['user_location'].astype('string')
df["user_description"] = df['user_description'].astype('string')
df["user_created"] = df['user_created'].astype('datetime64[ns]')
df["date"] = df['date'].astype('datetime64[ns]')

#- Crea una función que se encargue de mostrar cuántos tweets por ciudad han sido publicados

def agrupa_ubicacion_geografica():
    df_agrupado=df_covid.groupby(['user_location']).size().reset_index(name="count")
    return df_agrupado

tweets_por_ciudad = agrupa_ubicacion_geografica(df)
print(f'Tweets por ciudad \n{tweets_por_ciudad.head()}')

#- Crea una función que se encargue de mostrar una gráfica de barras con la información obtenida de la función anterior.