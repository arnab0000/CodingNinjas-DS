import matplotlib.pyplot as plt
import numpy as np
# x = [1, 2, 3]
# y = [2, 4, 6]
# plt.scatter(x, y)
# plt.show()
# employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
# year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
# revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]
# e = np.array(employees)
# y = np.array(year)
# r = np.array(revenue)
# plt.scatter(y, r, s = e)
# plt.grid()
# plt.show()
# i1 = np.where(y == 2008)
# i2 = np.where(y == 2015)
# print(2008, r[i1][0], e[i1][0])
# print(2015, r[i2][0], e[i2][0])
# company=['HP','Dell','Lenovo','Asus','Apple','Acer']
# sold=[20000,43000,15000,17000,22000,13000]
# c = np.array(company)
# s = np.array(sold)
# total = np.sum(s)
# plt.pie(sold, labels = company, autopct="%.1f")
# plt.axis("equal")
# plt.show()
# def getPercentage(n, total):
#     return format(((n / total) * 100), ".1f")
#
# for i in range(len(s)):
#     x = getPercentage(sold[i], total)
#     print(c[i], x)
height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
print(max(height))
print(min(height))
print(max(weight))
print(min(weight))
h = np.array(height)
w = np.array(weight)
# xt = np.arange(201)
plt.hist(h, bins=5, edgecolor="black", label="height")
plt.show()
plt.hist(w, bins=5, edgecolor="black", label="weight")
plt.show()