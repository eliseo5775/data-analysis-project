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

#- Crea una función que muestre cuántos tweets han sido publicados por mes, aparte muestrales en una tabla.

# - Crea una función que muestre cuántos tweets han sido publicados por semanas, basados en el punto anterior.

# - Crea una función que muestre cuales son las horas con más tweets basados en la división del punto anterior, ejemplo:
        # - Mañana entre 07-08 horas
        # - Tarde entre 15-16 horas
        # - Noche entre 21-22 horas

