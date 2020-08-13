import pandas as pd
import numpy as np
jobData = pd.read_csv("amazon_jobs_dataset.csv")
df = jobData.copy()
loactionBanglore = df[df["location"] == "IN, KA, Bangalore "]
loactionSeattle = df[df["location"] == "US, WA, Seattle "]
countB = loactionBanglore.shape[0]
# print(countB)
countS = loactionSeattle.shape[0]
print(countB, countS)