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

#Limpiamos strings
df["user_name"] = df['user_name'].str.lstrip()
df["user_location"] = df['user_location'].str.lstrip()
df["user_description"] = df['user_description'].str.lstrip()

#limpiamos NA
df = df.dropna(axis = 0)

# - Crea una función que se encargue de mostrar el total de tweets publicados con base en:
   # - Publicados con imágenes
   # - Publicados con urls
   # - Crea una función que se encargue de mostrar las palabras más repetidas por país.