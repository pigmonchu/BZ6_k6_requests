import requests

URL = "http://www.omdbapi1.com/?s={}&apikey=da22215a"

peli = input("Buscar: ")

respuesta = requests.get(URL.format(peli))

mijson = respuesta.json()

print(mijson.get("Search")[0].get("Title"))
print(mijson.get("Search")[0].get("Poster"))