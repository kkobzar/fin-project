import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# посилання на наш сайт
URL = "https://www.imdb.com/chart/top/"

MONGO_URL = "mongodb+srv://kkobzar:12345@cluster0.k2acs6d.mongodb.net/?retryWrites=true&w=majority"

# відправка зпапиту на сторінку
data = requests.get(URL).text

# парсимо сторінку
soup = BeautifulSoup(data, features="html.parser")

# знаходимо назви фільмів
films = soup.find_all("td", {"class": "titleColumn"})

# знаходимо рейтинг фільмів
ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

for f in films[0:10]:
  print(f.getText())

for r in ratings[0:10]:
  print(r.getText())

# підключаємось до нашої датабази
client = MongoClient(MONGO_URL)

db = client[""]
films = db[""]
films.insert_one({"film":"test"})
