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


#- Crea una función que muestre el resultado de cuántos usuarios por ciudad hay con publicación.

def agrupa_ubicacion_geografica(df):
    df_agrupado = df.groupby(['user_location']).size().reset_index(name="count")
    df_ordenado = df_agrupado.sort_values(['count'],ascending=[False])
    return df_ordenado


#- Crea una función que muestre cuales son los usuarios que han publicado más tweets.