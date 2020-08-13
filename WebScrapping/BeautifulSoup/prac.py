def intersection(arr1, arr2, n, m):
    i = 0
    j = 0
    arr1.sort()
    arr2.sort()
    while i < n and j < m:

        if arr1[i] > arr2[j]:
            j += 1

        else:
            if arr2[j] > arr1[i]:
                i += 1
            else:
                print(arr1[i], end=" ")
                i += 1
                j += 1

t = int(input())
while t > 0:
    n = int(input())
    if n > 0:
        arr1 = [int(i) for i in input().strip().split()]
    m = int(input())
    if m > 0:
        arr2 = [int(i) for i in input().strip().split()]
    if n != 0 and m != 0:
        intersection(arr1, arr2, n, m)
    t -= 1