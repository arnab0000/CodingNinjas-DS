import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
jobs = pd.read_csv("amazon_jobs_dataset.csv")
df = jobs.copy()
df["Index"] = df["location"].str.find("IN",start=0, end=2)
india = df[df["Index"] > -1]
india = india["location"].value_counts()
indices = india.index
vals = india.values
vals[3] += 1
total_jobs = np.sum(vals)
# print(indices, vals)
i = 0
while i < 5:
    jD = (vals[i] / total_jobs) * 100
    print(indices[i][8:], format(jD, ".2f"))
    i += 1
plt.pie(vals[:5])
plt.show()
