import pandas as pd
terrorismData = pd.read_csv('terrorismData.csv')
df = terrorismData.copy()
cData = df['Country'].value_counts()
country = cData.index[0]
number = cData.values[0]
iData = df[df.Country == country]
count = iData['Year'].value_counts()
print(count)
year = count.index[0]
print(country, number, year)