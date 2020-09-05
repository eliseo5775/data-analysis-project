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
#df = df.dropna(axis = 0)

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