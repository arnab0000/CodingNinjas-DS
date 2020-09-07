import sqlite3 as sq
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select genre.genre, earning.Domestic, earning.Worldwide from earning inner join genre on earning.Movie_id = genre.Movie_id', db)
data['Total'] = data['Domestic'] + data['Worldwide']
data['genre'].replace("", "0", inplace=True)
data = data[data['genre'] != "0"]
totalEarning = np.sum(data['Total'])
x = data.groupby('genre')['Total'].sum().sort_values(ascending=False)
vals = x.values
idx = x.index
valsModified = []
for i in range(len(vals)):
    a = format((vals[i] / totalEarning) * 100, ".2f")
    valsModified.append(a)
    print(idx[i], a)
plt.pie(valsModified, labels=idx)
plt.show()