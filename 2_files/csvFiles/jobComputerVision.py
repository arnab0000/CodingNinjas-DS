import pandas as pd
import numpy as np
jobData = pd.read_csv("amazon_jobs_dataset.csv")
df = jobData.copy()
cv = df[df["Title"].str.contains("Computer Vision")]
count = cv.shape[0]
print(count)