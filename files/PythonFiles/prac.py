hashMap = {}
n = int(input())
for i in range(n):
    arr = [int(i) for i in input().strip().split()]
    arr.sort()
    s = ""
    for i in range(len(arr)):
        s += str(arr[i])
    hashCode = hash(s)
    if hashCode in hashMap:
        hashMap[hashCode] += 1
    else:
        hashMap[hashCode] = 1

count = 0
for i in hashMap:
    if hashMap[i] == 1:
        count += 1
print(count)
