import urllib.request
import json

# Rotas Dinâmicas

def resultado_filmes(tipo):
    if tipo == "Populares":
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=687328d9e1f7fa5dba129c6a4d2bcd3e'
    elif tipo == "Animação":
        url = '<https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&with_genres=16&api_key=687328d9e1f7fa5dba129c6a4d2bcd3e>'
    elif tipo == "2010":
        url = '<https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=687328d9e1f7fa5dba129c6a4d2bcd3e>'

    response = urllib.request.urlopen(url)
    data = response.read()
    dados_json = json.loads(data)
    return dados_json['results']
    
# print(data_json['results'])

