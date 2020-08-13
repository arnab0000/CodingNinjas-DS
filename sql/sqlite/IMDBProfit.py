import sqlite3 as sq
import pandas as pd
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select IMDB.Title, IMDB.Budget, earning.Domestic, earning.Worldwide from IMDB inner join earning on IMDB.Movie_id = earning.Movie_id', db)
data['Budget'].replace("", "0", inplace=True)
data['Budget'].dropna(inplace=True)
convert_dict = {'Budget': float}
data = data.astype(convert_dict)
data['Profit'] = data['Domestic'] + data['Worldwide'] - data['Budget']
x = data.groupby(['Title', 'Profit'])['Budget'].min().sort_values(ascending=True)
print(x)