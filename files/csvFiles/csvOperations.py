import csv
import numpy as np
import pandas as pd
terrorismData = pd.read_csv("year2017.csv", skipinitialspace=True)
df = terrorismData.copy()
hash_country = []
country = df['Country'].values
for i in country:
    if i not in hash_country:
        hash_country.append(i)
for i in hash_country:
    data = df[df.Country == i]
    data['Country'].dropna(inplace=True)
    c = int(np.sum(data.casualities))
    print(i, c)