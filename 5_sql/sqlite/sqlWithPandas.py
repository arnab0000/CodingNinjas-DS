import sqlite3 as sq
import pandas as pd
db = sq.connect('IMDB.sqlite')
# data = pd.read_sql_query('show tables', db)
# print(data)
# data = pd.read_sql_query('select * from employee', db)
# print(data)
data = pd.read_sql_query('select genre.genre, count(IMDB.Title) from genre inner join IMDB on genre.Movie_id = IMDB.Movie_id group by genre.genre', db)
for i in data.values[1:]:
    print(i[0], i[1])
# print(data.values[1:])