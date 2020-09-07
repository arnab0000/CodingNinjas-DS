from collections import Counter
import pandas as pd
import numpy as np
terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()
df.Killed.fillna(0, inplace=True)
df.Wounded.fillna(0, inplace=True)
# convert_dict = {"Casualty": int}
df["Casualty"] = df["Killed"] + df["Wounded"]
# print(df.dtypes)
# df = df.astype(convert_dict)
df = df[df.Country == "India"]
df = df[["City", "Casualty"]]
# print(df.dtypes)
d = {}
df = df.values
for i in df:
    for j in range(1):
        if i[j] in d:
            d[i[j]] += i[1]
        else:
            d[i[j]] = i[1]
k = Counter(d)
highest = k.most_common(6)
for i in highest:
    if i[0] != "Unknown":
        print(i[0], int(i[1]))
