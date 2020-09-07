import pandas as pd
import numpy as np
terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()
df = df[(df.Day >= 10)]
df = df[(df.Day <= 20)]
print(df.shape[0])