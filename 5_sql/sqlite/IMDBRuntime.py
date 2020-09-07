import sqlite3 as sq
import pandas as pd
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query('select Title, Runtime from IMDB where Runtime is not NULL', db)
data['Runtime'].replace("", "0", inplace=True)
data['Runtime'].dropna(inplace=True)
def splitColumn(time):
    return time.split(" ")[0].strip()

data['Runtime'] = data['Runtime'].apply(splitColumn)
data['Runtime'].dropna(inplace=True)
convert_dict = {'Runtime': int}
data = data.astype(convert_dict)
x = data.groupby('Title')['Runtime'].max().sort_values(ascending=False)
runtime  = x.index[0]
print(runtime, x.values[0])
# d = {'Runtime' : int}
# data = data.astype(d)
# print(data)