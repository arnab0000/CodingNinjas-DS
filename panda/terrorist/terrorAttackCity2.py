import pandas as pd
terrorismData = pd.read_csv('terrorismData.csv')
df = terrorismData.copy()
iData = df[df.State == 'Jammu and Kashmir']
cData = iData['City'].value_counts()
city = cData.index
# print(city)
count = cData.values[0]
gData = df[df.City == city]
gData = gData['Group'].value_counts()
group = gData.index[1]
print(city, count, group)