from collections import Counter
import pandas as pd
import numpy as np
jobData = pd.read_csv("amazon_jobs_dataset.csv")
df = jobData.copy()
df['Index'] = df['location'].str.find("IN", start=0, end=2)
india = df[df['Index'] != -1]
x = {}
degree = india[(india["BASIC QUALIFICATIONS"].str.contains("Bachelor")) | (india["BASIC QUALIFICATIONS"].str.contains("BA")) | (india["BASIC QUALIFICATIONS"].str.contains("BS"))]
x['Python'] = degree[degree["BASIC QUALIFICATIONS"].str.contains("Python")].shape[0]
x['Java'] = degree[degree["BASIC QUALIFICATIONS"].str.contains("Java")].shape[0]
x['C++'] = degree[degree["BASIC QUALIFICATIONS"].str.contains("C+")].shape[0]
k = max(x, key=x.get)
print(k, x[k])

# python = degree[df]
# print(degree.shape[0])