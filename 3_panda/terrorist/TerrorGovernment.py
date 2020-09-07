import pandas as pd
terrorismData = pd.read_csv('terrorismData.csv')
df = terrorismData.copy()
df = df[df.Country == "India"]
df = df[df.Year >= 2014]
# print(df.head(406), df.Day)
# ways to remove data with multiple conditions
index1 = df[(df.Year == 2014) & (df.Month < 5)].index
index2 = df[(df.Year == 2014) & (df.Month == 5) & (df.Day < 26)].index
df.drop(index1, inplace= True)
df.drop(index2, inplace=True)
number = df.shape[0]
x = df.Group.value_counts()
# print(x)
print(number, x.index[1])



# print(df.Group)
# number = df.shape[0]
# gData = df['Group'].value_counts()
# print(gData)
# print(number, gData.index[1])