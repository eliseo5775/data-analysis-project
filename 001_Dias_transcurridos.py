# Ejecuta una función que calcule cuantos días transcurridos han pasado hasta
# el día que se ejecute, desde la primera vez que un usuario publicó un tweet
# acerca del CoronaVirus.
from datetime import date
import pandas as pd 

FILENAME = 'Dataset/covid19_tweets.csv'
df = pd.read_csv(FILENAME)

#Transformas la data
df["user_name"] = df['user_name'].astype('string')
df["date"] = df['date'].astype('datetime64[ns]')

#Exploramos la data
print(df.shape)
print(df.head())
print(df.info())
print(df.iloc[:,3:10])


def diastranscurridos(df_input001):
    
    current_date = date.today()
    print(current_date)
    return

diastranscurridos(df)