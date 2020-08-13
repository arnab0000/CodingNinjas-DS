import sqlite3 as sq
import pandas as pd
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select earning.Movie_id, earning.Domestic, earning.Worldwide, IMDB.rating from IMDB inner join earning on IMDB.Movie_id = earning.Movie_id', db)
data["Total"] = data["Domestic"] + data['Worldwide']
# print(data)
x = data.groupby('Rating')['Total'].max().sort_values(ascending=False)
rating = x.index[0]
print(rating)