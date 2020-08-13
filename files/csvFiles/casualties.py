import numpy as np
import pandas as pd
terrorismData = pd.read_csv("year2017.csv")
df = terrorismData.copy()
explosives = df[df['Weapon_type'] == 'Explosives']
wounded = int(np.sum(explosives.casualties))
print(wounded)
