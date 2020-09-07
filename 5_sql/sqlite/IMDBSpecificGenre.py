import sqlite3 as sq
import pandas as pd
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select genre.genre, IMDB.rating, IMDB.Title from IMDB inner join genre on IMDB.Movie_id = genre.Movie_id where IMDB.rating >= 8', db)
data = data[(data['genre'] == 'Sci-Fi') | (data['genre'] == 'Mystery')]
x = data['Title'].value_counts()
print(x.index[0])