import math

def sloveSecond(first, x, mu):
    return first + ((-1)**(mu + 1) * x**mu) / mu

print("Nhập x:")
x = float(input())
print("Nhập k:")
k = int(input())

mu = 2
first = x
second = sloveSecond(first, x, mu)

while math.fabs(first - second) > 10**(-k):
    mu = mu + 1
    first = second
    second = sloveSecond(first, x, mu)
    
print(f'{first:.3f}')