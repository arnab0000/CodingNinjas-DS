import sqlite3 as sq
import pandas as pd
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select IMDB.Title, earning.Domestic, earning.Worldwide from IMDB inner join earning on IMDB.Movie_id = earning.Movie_id', db)
data['Earning'] = data['Domestic'] + data['Worldwide']
data['Year'] = data['Title'].apply(lambda x: x[-5: -1])
data['Name'] = data['Title'].apply(lambda x: x[:-6].strip())
convert_dict = {'Year': int}
data = data.astype(convert_dict)
for i in range(2010, 2017, 1):
    x = data[data['Year'] == i]
    y = x.groupby('Name')['Earning'].max().sort_values(ascending=False)
    # print(y)
    print(i, y.index[0], len(y.index[0]))