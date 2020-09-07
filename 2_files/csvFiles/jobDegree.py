import pandas as pd
import numpy as np
jobData = pd.read_csv("amazon_jobs_dataset.csv")
df = jobData.copy()
df = df[df["location"].str.contains("IN")]
degree = df[(df["BASIC QUALIFICATIONS"].str.contains("Bachelor")) | (df["BASIC QUALIFICATIONS"].str.contains("BA")) | (df["BASIC QUALIFICATIONS"].str.contains("BS"))]
python = degree[df["BASIC QUALIFICATIONS"].str.contains("Python")]
java = degree[df["BASIC QUALIFICATIONS"].str.contains("Java")]
cpp = degree[df["BASIC QUALIFICATIONS"].str.contains("C++")]
pC = python.shape[0]
jC = java.shape[0]
cC = java.shape[0]
mC = max(pC, cC, jC)
print(pC, jC, cC, mC)