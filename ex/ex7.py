import math

def giaiThua(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return (n * giaiThua(n - 1))    

def sloveSecond(first, x, mu):
    return first + (x**(2 * mu) / giaiThua(2 * mu)) * (-1)**mu

print("Nhập x:")
x = float(input())
print("Nhập k:")
k = int(input())

x = x * math.pi / 180
mu = 1
first = 1
second = sloveSecond(first, x, mu)

while math.fabs(first - second) > 10**(-k):
    mu = mu + 1
    first = second
    second = sloveSecond(first, x, mu)
    
print(f'{first:.3f}')