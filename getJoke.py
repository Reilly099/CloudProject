#Gets a random joke from the joke api and writes it to a file

from urllib.request import urlopen
import requests

import json

url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"

response = requests.get(url)
jsondata = response.json()
jFile = open("jokeOfTheHour.txt", "w")
jFile.writelines(jsondata["joke"])
jFile.close()
