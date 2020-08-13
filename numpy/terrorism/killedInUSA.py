import pandas as pd
import numpy as np
terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()
df.Killed.fillna(0, inplace=True)
usaData = df[df.Country == "United States"]
usaKilled = usaData["Killed"].values
sum = int(np.sum(usaKilled))
print(sum)