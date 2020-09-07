import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
jobs = pd.read_csv("amazon_jobs_dataset.csv")
df = jobs.copy()
x, y = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], []
for i in x:
    ds = df[df["Posting_date"].str.contains(i)]
    count = ds.shape[0]
    y.append(count)

plt.bar(x, y)
plt.show()

j = 0
while j < len(x):
    print(x[j], y[j])
    j += 1