import math
# try:
#     a = int(input("Nhap a:"))
#     b = int(input("Nhap b:"))
# except ValueError:
#     print("Chi duoc nhap so !!")
# def InBangCuuChuong(a,b):
#     if(a>b):
#         InBangCuuChuong(b,a)
#     for i in range(a,b+1):
#         print(f'Bang Cuu Chuong {i}')
#         for j in range(1,11):
#             print(f'{i} x {j} = {i*j}')
# InBangCuuChuong(a,b)
#Kiem Tra So Nguyen To
# SoNguyenTo = lambda n : n >= 1 and len([x for x in range(2,round(math.sqrt(n))+1) if n%x==0]) == 0
# #Cau 2
# n = int(input("Nhap n1:"))
# print(SoNguyenTo(n))
# #Cau 3 va cau 4
# ListSoNTnhoHonN = [x for x in range(2,n) if SoNguyenTo(x)]
# print(ListSoNTnhoHonN)
# print(len(ListSoNTnhoHonN))
# #Cau 5
# ListUocSoLaSoNT = [x for x in range(2,n) if SoNguyenTo(x) and n%x == 0]
# print(ListUocSoLaSoNT)
#Phan Lambda
#Cau 1 
TriTuyetDoi = lambda n : n if n>=0 else -n
n = int(input("Nhap n:"))
print(TriTuyetDoi(n))
#Cau 2 
Cau2 = lambda n : n+15
#Cau 3
Tich = lambda x,y : x*y
#Cau 4
BoiSo13or19 = lambda n : n%13 == 0 or n%19 ==0
print(BoiSo13or19(26))
#Cau 5
DTHinhTron = lambda r : math.pi * (r*r)
#Cau 6
DtHCN = lambda d,r : (d+r)*2
#Cau 7
SoCPhuong = lambda n: math.sqrt(n) in [x for x in range(1,n)]
print(SoCPhuong(5))
#Cau 8 
SoNT = lambda n : n>=1 and len([x for x in range(math.sqrt(n)+1) if n%x == 0]) == 0
#Cau 9 
TamGiac = lambda x,y,z : "Tam Giac Deu" if(x==y==z) else "Tam Giac Vuong" if((sum([x**2 for x in [x,y,z]])-max([x,y,z])**2) == max([x,y,z])**2) else "Tam Giac Can" if(x==y or y==z or x==z) else "Tam Giac Thuong" if ((x+y) > z and (x+z)>y and (y+z)>x) else "Ko la tam giac"
print(TamGiac(4,4,5))
print(TamGiac(3,4,5))
print(TamGiac(5,5,5))
print(TamGiac(2,3,4))
print(TamGiac(50,2,3))


