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

def agrupa_por_mes (df_in004):
        df_mes = df_in004.groupby(df['date'].dt.strftime('%B')).size().reset_index(name="count")
        df_order = df_mes.sort_values(['count'],ascending=[False])
        return df_order

top_mes = agrupa_por_mes(df)

print(f'Estos son los tweets meses\n{top_mes}')
top_mes.plot(kind='bar',x='date',y='count',title = '# Tweets por mes')
plt.show()


# - Crea una función que muestre cuántos tweets han sido publicados por semanas, basados en el punto anterior.

def agrupa_por_sem (df_in004):
        df_mes = df_in004.groupby(df['date'].dt.strftime('%U')).size().reset_index(name="count")
        return df_mes

top_sem = agrupa_por_sem(df)

print(f'Estos son los tweets por semana\n{top_sem}')
top_sem.plot(kind='bar',x='date',y='count',title = '# Tweets por Semana')
plt.show()

# - Crea una función que muestre cuales son las horas con más tweets basados en la división del punto anterior, ejemplo:
        # - Mañana entre 07-08 horas
        # - Tarde entre 15-16 horas
        # - Noche entre 21-22 horas

def agrupa_por_hr (df_in004):
        df_hr = df_in004.groupby(df['date'].dt.strftime('%H')).size().reset_index(name="count")
        return df_hr

top_hr = agrupa_por_hr(df)

print(f'Estos son los tweets por horario\n{top_hr}')
top_hr.plot(kind='bar',x='date',y='count',title = '# Tweets por hora')
plt.show()
