import requests
from bs4 import BeautifulSoup
import json
import logging

url = "https://www.nytimes.com/crosswords/game/mini"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tablo = soup.find_all("section",{"class":"Layout-clueLists--10_Xl"})

print(tablo[0].text)

