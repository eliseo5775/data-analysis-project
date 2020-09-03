# Descarga de data de dataset de twetts http://galileoguzman.com/data/covid19_tweets.csv
import requests
import pandas as pd
from datetime import datetime, date

#df_web = requests.get('http://galileoguzman.com/data/covid19_tweets.csv')
#print(df_web.status_code)

#Ejercicio 1 ###############################################################################

#leer de CSV

FILENAME = 'Dataset/covid19_tweets.csv'
df = pd.read_csv(FILENAME)

#Transformas la data 
df["user_name"] = df['user_name'].astype('string')
df["user_location"] = df['user_location'].astype('string')
df["user_description"] = df['user_description'].astype('string')
df["user_created"] = df['user_created'].astype('datetime64[ns]')
df["date"] = pd.to_datetime(df['date'].astype('datetime64[ns]'))

#Limpiamos strings
df["user_name"] = df['user_name'].str.lstrip()

#limpiamos NA
df = df.dropna(axis = 0)

#Exploramos la data
print(f'\nShape del data frame:\n\n{df.shape}')
print(f'\nInfo del data frame:\n\n{df.info()}')
print(f'\nHead del data frame:\n\n{df.head()}')



# Ejecuta una función que calcule cuantos días transcurridos han pasado hasta
# el día que se ejecute, desde la primera vez que un usuario publicó un tweet
# acerca del Coronavirus.

def diastranscurridos(df_in001):
    # limpiar el data set y quitar columnas feas, ademas transoformamos
    df_cl_in001 = df_in001.drop(columns=['user_followers','user_location','user_friends','user_favourites','user_description','user_created','source','is_retweet','text','user_verified','hashtags'])
    #date min por usuario
    df_grp_min = df_cl_in001.loc[df_in001.groupby('user_name').date.idxmin()]
    #agregamos el current date
    current_date = pd.to_datetime(date.today())
    df_grp_min.insert(2,'today_date',current_date)
    #calculamos los dias entre dos fechas y agregamos columna
    df_dias_trans = df_grp_min['today_date']-df_grp_min['date']
    # convertimos a frame
    df_dias_trans = df_dias_trans.to_frame()
    # agregar la columna de dias trans 
    df_grp_min["dias_transcurridos"] = df_dias_trans
    return(df_grp_min)

#Ejecutamos función
df_dias_trans = diastranscurridos(df)
print(f'Los dias transcurridos desde el primer tweet de cada usuario son los siguientes \n______________________________________________\n{df_dias_trans}')


#Ejercicio 2 ###############################################################################

#Ejercicio 3 ###############################################################################

#Ejercicio 4 ###############################################################################

#Ejercicio 5 ###############################################################################