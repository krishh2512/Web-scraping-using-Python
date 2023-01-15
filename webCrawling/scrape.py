import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = []
for tr in soup.find_all("tr")[1:]:
    title = tr.find("td", class_="titleColumn").find("a").get_text()
    rating = tr.find("td", class_="ratingColumn").find("strong").get_text()
    movies.append([title, rating])

with open("movies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Rating"])
    writer.writerows(movies)
