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

#- Crea una función que se encargue de mostrar cuántos tweets por ciudad han sido publicados

def agrupa_ubicacion_geografica(df):
    df_agrupado = df.groupby(['user_location']).size().reset_index(name="count")
    df_ordenado = df_agrupado.sort_values(['count'],ascending=[False])
    return df_ordenado

tweets_por_ciudad = agrupa_ubicacion_geografica(df)
print(f'Tweets por ciudad \n{tweets_por_ciudad}')

#- Crea una función que se encargue de mostrar una gráfica de barras con la información obtenida de la función anterior.
def grafica_ubicación_geografica(df_in002):
    df_in002.plot(kind='bar',x='user_location',y='count', title = '# Tweets por ciudad')
    return plt.show()

grafica_ubicación_geografica(tweets_por_ciudad.iloc[1:50,:])


#Ejercicio 3 ###############################################################################

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

#Exploramos la data
print(f'Shape del data frame:\n{df.shape}')
print(f'Head del data frame:\n{df.head()}')
print(f'Info del data frame:\n{df.info()}')

#- Crea una función que muestre el resultado de cuántos usuarios por ciudad hay con publicación.

def agrupa_rt_location(df):
    #filtrar los que no son retweet
    df_isrt = df['is_retweet'] == False
    df_filtrado = df[df_isrt]
    #filtrar usuarios unicos
    df_filtrado = df_filtrado.drop_duplicates(subset=['user_name'])
    #agrupar por user location
    df_grouped = df_filtrado.groupby(['user_location']).size().reset_index(name="count")
    df_order = df_grouped.sort_values(['count'],ascending=[False])

    df_order = df_order.iloc[1:20,:]
    return df_order

df_filter = agrupa_rt_location(df)

print(f'El data frame filtrado con el top 20 de ciudades \n{df_filter}')

df_filter.plot(kind='bar',x='user_location',y='count',title = '# De Usuarios Unicos con publicación del Top 20 de Ciudades')
plt.show()

#- Crea una función que muestre cuales son los usuarios que han publicado más tweets.

def agrupa_top_user(df):
    #filtrar los que no son retweet
    df_grouped = df.groupby(['user_name']).size().reset_index(name="count")
    df_order = df_grouped.sort_values(['count'],ascending=[False])
    df_order1 = df_order.iloc[1:10,:]
    return df_order1

top_user = agrupa_top_user(df)

print(f'Estos son los top 10 Users\n{top_user}')
top_user.plot(kind='bar',x='user_name',y='count',title = '# Top 10 de Usuarios con Mas tweets')
plt.show()

#Ejercicio 4 ###############################################################################

#Ejercicio 5 ###############################################################################