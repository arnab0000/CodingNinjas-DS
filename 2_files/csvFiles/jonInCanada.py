import pandas as pd
import numpy as np
jobData = pd.read_csv("amazon_jobs_dataset.csv")
df = jobData.copy()
df["Index"] = df["location"].str.find("CA", start=0, end=2)
canada = df[df["Index"] != -1]
print(canada.shape[0])
# print(canada)
# count = canada.shape[0]
# print(count)