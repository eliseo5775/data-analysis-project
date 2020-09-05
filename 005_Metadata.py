#import requirements
from datetime import date
from collections import Counter
import pandas as pd 
import matplotlib.pyplot as plt

FILENAME = 'Dataset/covid19_tweets.csv'
df = pd.read_csv(FILENAME)

#Transformas la data
df["user_name"] = df['user_name'].astype('str')
df["user_location"] = df['user_location'].astype('str')
df["user_description"] = df['user_description'].astype('str')
df["text"] = df['text'].astype('str')
df["user_created"] = df['user_created'].astype('datetime64[ns]')
df["date"] = df['date'].astype('datetime64[ns]')

#Limpiamos strings
df["user_name"] = df['user_name'].str.lstrip()
df["user_location"] = df['user_location'].str.lstrip()
df["user_description"] = df['user_description'].str.lstrip()

#limpiamos NA
#df = df.dropna(axis = 0)

# - Crea una función que se encargue de mostrar el total de tweets publicados con base en:
   # - Publicados con imágenes
   # - Publicados con urls

def tiene_url (df):
    #filtrar los que tienen URL
    df_url = df['text'].str.contains('https')
    return df_url

df_url = tiene_url(df)

numero_url = len(df_url.index)

print(f'{numero_url} tweets contienen URL')

# - Crea una función que se encargue de mostrar las palabras más repetidas por país.
def mas_frecuente (df_in006):
   df_mf = Counter(" ".join(df_in006["text"]).split()).most_common(10)
   return df_mf

print(f'Top 10 palabras mas frecuentes \n {mas_frecuente(df)}')