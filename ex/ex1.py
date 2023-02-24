import math

def giaiThua(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return (n * giaiThua(n - 1))    

def solveSecond(first, x, mu):
    return first + x**mu / giaiThua(mu)

print("Nhập x:")
x = float(input())
print("Nhập k:")
k = int(input())

mu = 1
first = 1
second = solveSecond(first, x, mu)

while math.fabs(first - second) > 10**(-k):
    mu = mu + 1
    first = second
    second = solveSecond(first, x, mu)
    
print(f'{first:.3f}')