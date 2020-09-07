import pandas as pd
import numpy as np
terrorismData = pd.read_csv('terrorismData.csv')
df = terrorismData.copy()
# jnkData = df[df.State == 'Jammu and Kashmir']
# jData = df[df.State == 'Jharkhand']
# cData = df[df.State == 'Chattisgarh']
# oData = df[df.State == 'Odisha']
# apData = df[df.State == 'Andhra Pradesh']
# jData = jData[['Killed', 'Wounded']]
# oData = oData[['Killed', 'Wounded']]
# ckData = cData[['Killed', 'Wounded']]
# apData = apData[['Killed', 'Wounded']]
# jnkData = jnkData[['Killed', 'Wounded']]
# numberinJNK = jnkData.sum(axis = 0, skipna = True)
# numberinJ = jData.sum(axis = 0, skipna = True)
# numberinO = oData.sum(axis = 0, skipna = True)
# numberinC = cData.sum(axis = 0, skipna = True)
# numberinAP = apData.sum(axis=0, skipna= True)
# numberinJ = numberinJ.values
# numberinJ = numberinJ[0] + numberinJ[1]
# numberinO = numberinO.values
# numberinO = numberinO[0] + numberinC[1]
# numberinC = numberinC.values
# numberinC = numberinC[0] + numberinC[1]
# numberinAP = numberinAP.values
# numberinAP = numberinAP[0] + numberinAP[1]
# #numberinRCS = rcsData.sum(axis = 0, skipna = True)
# # print(numberinRCS)
# numberinJNK = numberinJNK.values
# numberinJNK = numberinJNK[0] + numberinJNK[1]
# # print(numberinJNK, numberinJ, numberinC, numberinO, numberinAP)
# numberinRCS = numberinJ + numberinC + numberinO +numberinAP
# # numberinRCS = numberinRCS.values
# # print(numberinRCS)
# # numberinRCS = numberinRCS[0] + numberinRCS[1]
# # print(numberinRCS)
# # print(rcsData)
# # print(numberinJNK)
# frequencyJNK = int(numberinJNK / numberOfYears)
# frequencyRCS = int(numberinRCS / numberOfYears)
# print(frequencyRCS, frequencyJNK)
year = len(set(df.Year))
df = df[df.Country == 'India']
df['Casualty'] = df['Killed'] + df['Wounded']
jnkData = df[df.State == 'Jammu and Kashmir']
rcsData = df[(df['State'] == 'Odisha') | (df['State'] == 'Jharkhand') | (df['State'] == 'Andhra Pradesh') | (df['State'] == 'Chattisgarh')]
rcsC = int(np.sum(rcsData.Casualty))
jnkC = int(np.sum(jnkData.Casualty))
print(rcsC // year, jnkC // year)