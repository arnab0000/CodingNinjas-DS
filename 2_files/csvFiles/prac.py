# #input size of array
# n = int (input ('Array size : ' ))
# #input list elements separated by a space
# lst = input ('list elements : ' )
# elements = lst.split()
# x = []
# for i in elements:
#     x.append(int(i))
# sum = 0
# for i in x:
#     sum = sum + i
#
# print (sum)
# print (elements)
x = [int(i) for i in input().strip().split()]
print(x)