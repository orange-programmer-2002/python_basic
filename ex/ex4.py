import math

def giaiThua(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return (n * giaiThua(n - 1))

def topSlove(mu):
    return 1/2 * (1/2 - mu + 1)

def sloveSecond(first, top, x, mu):
    return first + (top / giaiThua(mu)) * x**mu

print("Nhập x:")
x = float(input())
print("Nhập k:")
k = int(input())

mu = 2
first = 1 + 1/2 * x
top = topSlove(mu)
second = sloveSecond(first, top, x, mu)

while math.fabs(first - second) > 10**(-k):
    mu = mu + 1
    first = second
    top = top * topSlove(mu)
    second = sloveSecond(first, top, x, mu)
    
print(f'{first:.3f}')   