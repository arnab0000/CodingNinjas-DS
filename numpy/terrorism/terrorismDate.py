import pandas as pd
import numpy as np
terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()
df = df[df.Year == 2010]
df = df[df.Month == 1]
df = df.values
# print(df)
print(df.shape)