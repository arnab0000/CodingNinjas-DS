import pandas as pd
import numpy as np
terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()
df.Killed.fillna(0, inplace=True)
df.Wounded.fillna(0, inplace=True)
df["Casualty"] = df["Killed"] + df["Wounded"]
df = df[(df['State'] == 'Odisha') | (df['State'] == 'Jharkhand') | (df['State'] == 'Andhra Pradesh') | (df['State'] == 'Chhattisgarh')]
count = int(np.sum(df["Casualty"]))
print(count)