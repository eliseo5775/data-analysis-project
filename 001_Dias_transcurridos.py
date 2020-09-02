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
print(df.shape)
#print(df.head())
print(df.info())
#print(df.iloc[1:5,5:13])


def diastranscurridos(df_in001):
    # limpiar el data set y quitar columnas feas
    df_cl_in001 = df_in001.drop(columns=['user_followers','user_friends','user_favourites','user_description','user_created','source','is_retweet','text','user_verified','hashtags'])
    #date min por usuario
    df_grp_min = df_cl_in001.loc[df_in001.groupby('user_name').date.idxmin()]
    #agregamos el current date
    current_date = date.today().apply(pd.to_datetime)
    df_grp_min.insert(3,'today_date',current_date)
    #Transformamos a date time 
    #calculamos los dias entre dos fechas y agregamos columna
    df_dias_trans = df_grp_min['today_date']-df_grp_min['date']
    print(f'DF agrupado \n {df_grp_min.head()} \n ,{df_grp_min.shape}')
    return(df_dias_trans)

df_dias_trans = diastranscurridos(df)
#print(f'la fecha de hoy es \n{today}')