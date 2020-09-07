import sqlite3 as sq
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select genre.genre, IMDB.budget from IMDB inner join genre on IMDB.Movie_id = genre.Movie_id', db)
data['Budget'].replace("", "0", inplace=True)
data['Budget'].dropna(inplace=True)
convert_dict = {'Budget': int}
data = data.astype(convert_dict)
data['genre'].replace("", "0", inplace=True)
data = data[data['genre'] != "0"]
x = data.groupby('genre')['Budget'].sum().sort_values(ascending=False)
totalBudget = np.sum(data['Budget'])
# x['Budget'].apply(lambda x: (x / totalBudget) * 100)
# # print(totalBudget)
idx = x.index
vals = x.values
valsModified = []
for i in range(len(vals)):
    a = format((vals[i] / totalBudget) * 100, ".2f")
    valsModified.append(a)
    print(idx[i], a)
plt.pie(valsModified, labels=idx)
plt.show()