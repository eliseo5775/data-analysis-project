
from datetime import date
import pandas as pd 

FILENAME = 'Dataset/covid19_tweets.csv'
df = pd.read_csv(FILENAME)

#Transformas la data con el casting
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
print(df.shape)
#print(df.head())
print(df.info())
#print(df.iloc[1:5,5:13])

# Ejecuta una función que calcule cuantos días transcurridos han pasado hasta
# el día que se ejecute, desde la primera vez que un usuario publicó un tweet
# acerca del CoronaVirus.

def diastranscurridos(df_in001):
    # limpiar el data set y quitar columnas feas
    df_cl_in001 = df_in001.drop(columns=['user_followers','user_friends','user_favourites','user_description','user_created','source','is_retweet','text','user_verified','hashtags'])
    #date min por usuario
    df_grp_min = df_cl_in001.loc[df_in001.groupby('user_name').date.idxmin()]
    #agregamos el current date
    current_date = date.today()
    df_grp_min.insert(3,'today_date',current_date)
    print(f'DF con current date \n {df_grp_min.head()} \n ,{df_grp_min.shape}')
    #calculamos los dias entre dos fechas y agregamos columna
    df_dias_trans = "df_grp_min.list(df_grp_min['today_date']-df_grp_min['date'])"
    return(df_dias_trans)

df_dias_trans = diastranscurridos(df)
print(f'Los dias transcurridos por usuario son los siguientes \n______________________________________________\n{df_dias_trans}')