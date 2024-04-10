from bs4 import BeautifulSoup
import requests

data = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
data_txt = data.text

soup = BeautifulSoup(data_txt,"html.parser")
# print(soup)
# print(soup.prettify())

soup_extract = soup.find_all('h3', class_= 'listicleItem_listicle-item__title__BfenH')
# print(soup_extract)

movie_titles = [movie.getText() for movie in soup_extract]
# print(movie_titles)

movies_accending = movie_titles[::-1]
# print(movies_accending)

with open("film_names.txt", mode="w") as file:
    for movie in movies_accending:
        file.write(f"{movie}\n")
