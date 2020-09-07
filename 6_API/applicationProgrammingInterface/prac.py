def checkArmstrong(n):
    lst = []
    while n > 0:
        r = n % 10
        n = n // 10
        lst.append (r)
    return lst

def isArmstrong(n):
    x = checkArmstrong(n)
    armstrong = 0
    for i in range(len(x)):
        result = pow (x[i], len(x))
        armstrong = armstrong + result
    if armstrong == n:
        return True
    return False

n=int(input())
if isArmstrong(n):
    print ('true')

else:
    print ('false')