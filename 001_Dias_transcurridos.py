# Ejecuta una función que calcule cuantos días transcurridos han pasado hasta
# el día que se ejecute, desde la primera vez que un usuario publicó un tweet
# acerca del CoronaVirus.
from datetime import date
import pandas as pd 

FILENAME = 'Dataset/covid19_tweets.csv'
df = pd.read_csv(FILENAME)

#Transformas la data
df["user_name"] = df['user_name'].astype('string')
df["user_location"] = df['user_location'].astype('string')
df["user_description"] = df['user_description'].astype('string')
df["user_created"] = df['user_created'].astype('datetime64[ns]')
df["date"] = df['date'].astype('datetime64[ns]')

#Exploramos la data
#print(df.shape)
#print(df.head())
#print(df.info())
#print(df.iloc[1:5,5:13])


def diastranscurridos(df_in001):
    #current date
    #current_date = date.today()
    #date min por usuario
    df_grp_min = df_in001.loc[df_in001.groupby('user_name').date.idxmin()]
    print(f'DF agrupado \n {df_grp_min.head()}')
    return()

today = diastranscurridos(df)
#print(f'la fecha de hoy es \n{today}')