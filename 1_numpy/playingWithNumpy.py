import numpy as np
# print(np.arange(9, 50, 1, dtype=int))
# print(np.eye(3, 4, dtype=int))
# x = 5 / 9
# sum = 0
# for i in range(10):
#     sum += x
#     print(format(sum, '.2f'))
# # print(np.linspace(0, 5, 9))
# input_=np.arange(1,21,1)
# input_ = input_.reshape(4,5)
# x1 = input_[2, :3]
# for i in x1:
#     print(i, end = " ")
# print()
# x2 = input_[1: , 3]
# for i in x2:
#     print(i, end = " ")
# print()
# x4 = input_[2:, 0: ]
# for i in x4:
#     for j in i:
#         print(j, end = " ")
# print()
# x3 = input_[1:3, 1:3]
# for i in x3:
#     for j in i:
#         print(j, end = " ")
# a = [1, 2, 0, 0, 4, 0]
# a = np.array(a)
# index = np.where(a > 0)
# for i in index:
#     x = i
# for i in x:
#     print(x)
# # print(index)
# a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# a = np.array(a)
# a = a % 3
# print(a)
# index = np.where(a < 1)
# for i in index[0]:
#     print(i, end = " ")
# index = np.where(a % 3)
# for i in index[0]:
#     print(i, end = " ")
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = np.array(a)
# index = np.where(a[(a >= 3) & (a <= 8)])
# print(index)
# a[index] -= 1
# print(a)
# print(newArr)
import numpy as np
a = [[21,20,19,18,17],
  [16,15,14,13,12],
  [11,10,9,8,7],
  [ 6,5,4,3,2]]
a.sort()
a = np.array(a)
print(a)