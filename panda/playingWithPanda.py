import pandas as pd
column_name = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
#importing data with the column names
iris = pd.read_csv("iris.data", names=column_name)
#making a copy so that we cannot change the the iris data base
df = iris.copy()
# print(df.iloc[53:56, 4])
type1 = df[df.Species == "Iris-setosa"]
type2 = df[df.Species == "Iris-virginica"]
type3 = df[df.Species == "Iris-versicolor"]
t3 = type3.describe().values
t1 = type1.describe().values
t2 = type2.describe().values
# print(type1.describe())
for i in t1[3]:
    print(format(i, '.2f'), end = " ")
print('Iris-setosa')
for i in t1[7]:
    print(format(i, '.2f'), end = " ")
print('Iris-setosa')
for i in t1[1]:
    print(format(i, '.2f'), end = " ")
print('Iris-setosa')
for i in t3[3]:
    print(format(i, '.2f'), end = " ")
print('Iris-versicolor')
for i in t3[7]:
    print(format(i, '.2f'), end = " ")
print('Iris-versicolor')
for i in t3[1]:
    print(format(i, '.2f'), end = " ")
print('Iris-versicolor')
for i in t2[3]:
    print(format(i, '.2f'), end = " ")
print('Iris-virginica')
for i in t2[7]:
    print(format(i, '.2f'), end = " ")
print('Iris-virginica')
for i in t2[1]:
    print(format(i, '.2f'), end = " ")
print('Iris-virginica')
