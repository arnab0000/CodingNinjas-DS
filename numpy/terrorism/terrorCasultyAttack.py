import pandas as pd
import numpy as np
terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()
df.Killed.fillna(0, inplace=True)
df.Wounded.fillna(0, inplace=True)
df["Casualty"] = df['Killed'] + df["Wounded"]
df = df[df.State == "Jammu and Kashmir"]
df = df[df.Year == 1999]
df = df[df.Month >= 5]
df = df[df.Month <= 7]
# print(df)
# numbers = df["Casualty"].value_counts()
df = df[["City", "Casualty", "Group"]]
required = df[df["Casualty"] == max(df["Casualty"])]
x = required.values[0]
print(x[1], x[0], x[2])
# index = max(df["Casualty"])
# print(index)
# numbers = max(df["Casualty"])
# print(numbers)