import pandas as pd
terrorismData = pd.read_csv('terrorismData.csv')
df = terrorismData.copy()
df = df[df.Killed == max(df.Killed)].values
print(int(df[0][10]), df[0][3], df[0][-3])
