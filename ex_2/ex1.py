with open('D:\input.txt', 'r') as f:
    arr = []
    for line in f:
        row = [int(x) for x in line.split()]
        arr.append(row)  
  
def check_prime_number(n):
    flag = 1;
    if (n <2):
        flag = 0
        return flag
    
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag
      
# 1.a
def ex1a():
    demChan = 0
    demLe = 0
    for row in arr:
        for element in row:
            if (element % 2 == 0):
                demChan += 1
            else:
                demLe += 1                
    print(f"Có {demChan} số chẵn và {demLe} số lẻ")

# 1.b   
def ex1b():
    dem = 0
    for row in arr:
        for element in row:
            if (check_prime_number(element) != 0):
                dem += 1     
    print(f"Có {dem} số nguyên tố") 
    
# 1.c
def ex1c():
    demMax = 0
    luuSo = None
    for row in arr:
        for element in row:
            dem = row.count(element)
            if dem > demMax:
                demMax = dem
                luuSo = element
    print(f"Số {luuSo} xuất hiện {demMax}") 