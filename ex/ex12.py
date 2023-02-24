import math

def sloveSecond(first, x, mu):
    return first + (x**(2 * mu + 1) / (2 * mu + 1))

print("Nhập x:")
x = float(input())
print("Nhập k:")
k = int(input())

mu = 1
first = x
second = sloveSecond(first, x, mu)

while math.fabs(first - second) > 10**(-k):
    mu = mu + 1
    first = second
    second = sloveSecond(first, x, mu)
    
first = first * 2
    
print(f'{first:.3f}')