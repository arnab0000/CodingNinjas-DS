import pandas as pd
import numpy as np
jobData = pd.read_csv("amazon_jobs_dataset.csv")
df = jobData.copy()
df['BASIC QUALIFICATIONS'].dropna(inplace=True)
df["Index"] = df["BASIC QUALIFICATIONS"].str.find("Java")
java = df[df["Index"] != -1]
df1 = java["location"]
df1["Index2"] = df1["location"].str.find("US", start=0, end=2)
df1 = df1[df1["Index2"] != 1]
df1 = df1["location"]
x = df1.shape[0]
print(x)
