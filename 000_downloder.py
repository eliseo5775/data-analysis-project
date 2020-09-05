import requests

# Constantes
URL_BASE = "https://galileoguzman.com/data/covid19_tweets.csv"

def get_data():
    response = requests.get(URL_BASE)
    if response.status_code == 200:
        response_content = response.content
        filename = "Dataset/covid19_tweets.csv"
        with open(filename, "wb") as archivo:
            archivo.write(response_content)
            return archivo
    return None

# Descargar el archivo y guardarlo en local
get_data() 