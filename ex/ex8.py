import math

def giaiThua(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return (n * giaiThua(n - 1))  

def solveSecond(first, x, mu):
    return first + ((2 * mu) / (2**mu * giaiThua(mu))**2) * (x**(2 * mu + 1) / (2 * mu + 1))

print("Nhập x:")
x = float(input())
print("Nhập k:")
k = int(input())

mu = 1
first = x
second = solveSecond(first, x, mu)

while first - second > 10**(-k):
    mu = mu + 1
    first = second
    second = solveSecond(first, x, mu)
    
print(f'{first:.3f}')