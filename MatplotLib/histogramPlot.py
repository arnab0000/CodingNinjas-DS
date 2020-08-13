import matplotlib.pyplot as plt
import numpy as np
height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
h = np.array(height)
w = np.array(weight)
# xt = np.arange(201)
plt.hist(h, bins=5, edgecolor="black", label="height")
plt.show()
plt.hist(w, bins=5, edgecolor="black", label="weight")
plt.show()
print(184, 89)