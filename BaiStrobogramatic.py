from math import sqrt    
def IsStrobogrammaticCauE(num,NumberOfStrobogrammatic):
    numberRotated = []
    temp = num
    while num > 0:
        digit = num%10
        if digit not in NumberOfStrobogrammatic:
            return False
        else:
            if digit not in [6,9]:
                numberRotated.append(digit)
            if digit == 9:
                numberRotated.append(6)
            if digit == 6:
                numberRotated.append(9)
        num = num//10
    numberRotated = "".join(map(str,numberRotated))
    if int(numberRotated) != temp and IsPrimeNumber(int(numberRotated)):
        return True
    return False
def IsStrobogrammatic(num,NumberOfStrobogrammatic):
    numberRotated = []
    temp = num
    while num > 0:
        digit = num%10
        if digit not in NumberOfStrobogrammatic:
            return False
        else:
            if digit not in [6,9]:
                numberRotated.append(digit)
            if digit == 9:
                numberRotated.append(6)
            if digit == 6:
                numberRotated.append(9)
        num = num//10
    numberRotated = "".join(map(str,numberRotated))
    if int(numberRotated) == temp:
        return True
    return False
def IsPrimeNumber(num):
    if (num <= 3):
        return True
    for i in range(2,round(sqrt(num))+1):
        if num % i == 0:
            return False
    return True
#Bai 119
#Cau a
NumberOfStrobogrammatic = [0,1,8,6,9]
NumberOfStrobogrammaticOpen = [0,1,2,5,8,6,9]
# print("Cau A : ")
# for i in range(1,1000000):
#     if IsStrobogrammatic(i,NumberOfStrobogrammatic):
#         print(i)
#Cau b
# print("Cau B : ")
# for i in range(1,1000000):
#     if IsStrobogrammatic(i,NumberOfStrobogrammatic) and IsPrimeNumber(i):
#         print(i)
# #Cau c
# print("Cau C : ")
# for i in range(1,1000000):
#     if IsStrobogrammatic(i,NumberOfStrobogrammaticOpen):
#         print(i)
# print("Cau D : ")
# for i in range(1,1000000):
#     if IsStrobogrammatic(i,NumberOfStrobogrammaticOpen) and IsPrimeNumber(i):
#         print(i)
print("Cau E : ")
for i in range(1,10000):
    if IsStrobogrammaticCauE(i,NumberOfStrobogrammatic):
        print(i)
#Bai 121
try:
    n = int(input("Nhap n (2<=n<=10): "))
    if n not in [x for x in range(2,10)]:
        print("da vuot qua gioi han")
    else:
        print("Cau a: ")
        for i in range(10**(n-1),10**n):
            if IsStrobogrammatic(i,NumberOfStrobogrammatic):
                print(i)
        print("Cau b: ")
        for i in range(10**(n-1),10**n):
            if IsStrobogrammatic(i,NumberOfStrobogrammaticOpen):
                print(i)
except ValueError:
    print("Sai dinh dang")