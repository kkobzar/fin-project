import requests
from bs4 import BeautifulSoup

# посилання на наш сайт
URL = "https://www.imdb.com/chart/top/"

# відправка зпапиту на сторінку
data = requests.get(URL).text

# парсимо сторінку
soup = BeautifulSoup(data, features="html.parser")


print(soup.find_all("td"))