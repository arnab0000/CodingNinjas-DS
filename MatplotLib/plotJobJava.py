import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
jobs = pd.read_csv("amazon_jobs_dataset.csv")
df = jobs.copy()
java = df[(df["BASIC QUALIFICATIONS"].str.contains("Java")) | (df["BASIC QUALIFICATIONS"].str.contains("java"))]
x, y = [], []
for i in range(2011, 2019, 1):
    year = str(i)
    ds = java[java["Posting_date"].str.contains(year)]
    count = ds.shape[0]
    y.append(count)
    x.append(i)
j = 0
while j < len(x):
    print(x[j], y[j])
    j += 1
plt.scatter(x, y)
plt.show()