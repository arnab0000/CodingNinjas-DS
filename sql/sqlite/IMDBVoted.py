import sqlite3 as sq
import pandas as pd
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select TotalVotes, Rating, Title from IMDB', db)
x = data.groupby(['Rating', 'Title'])['TotalVotes'].max().sort_values(ascending=False)
print(x.index[0][1], x.index[0][0])
# print(x)