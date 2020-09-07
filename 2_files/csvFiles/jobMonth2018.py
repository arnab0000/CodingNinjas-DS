import pandas as pd
import numpy as np
jobData = pd.read_csv("amazon_jobs_dataset.csv")
df = jobData.copy()
posting_date = df[df["Posting_date"].str.contains("2018")]
jan = posting_date[posting_date["Posting_date"].str.contains("January")]
count = jan.shape[0]
print("January", count)