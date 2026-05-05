import math
nhaptiep = True
lst = []
while(nhaptiep):
    num = int(input())
    lst.append(num)
    while(True):
        query = input("Ban co muon nhap tiep khong ?(Nhap Y(yes) hoac N(no)) :")
        query = query.upper()
        if query not in ["N","Y"]:
            print("Chi nhap Y hoac N. Nhap lai")
            continue
        if query == "N":
            nhaptiep=False
        break
# Cau a
def LasoNguyenTo(num):
    if num <= 3:
        return True
    for i in range(2,math.isqrt(num)):
        if num % i == 0:
            return False
    return True
print("So nguyen to co trong LIST : ",end="")
for item in lst:
    if LasoNguyenTo(item):
        print(item,end=" ")
print()
#Cau b
lstSoAm = list(filter(lambda x : x < 0 ,lst))
if len(lstSoAm) == 0:
    lstSoAm.append(0)
print(f'Trung binh cong so am trong List = {sum(lstSoAm)/len(lstSoAm)}')
lstSoDuong = list(filter(lambda x: x >= 0 ,lst))
if len(lstSoDuong) == 0:
    lstSoDuong.append(0)
print(f'Trung binh cong so am trong List = {sum(lstSoDuong)/len(lstSoDuong)}')
#Cau c
lstSort =lst.copy()
lstSort.sort()
print(f'So nho nhat = {lstSort[0]} va So lon nhat = {lstSort[len(lst)-1]}')

#Cau d
tangdan = True
for i in range(len(lst)-1,0,-1):
    if(lst[i] < lst[i-1]):
        print("Mang chua sap xep tang dan!!!")
        tangdan = False
        break
if tangdan is True:
    print("Mang da sap xep tang dan!!!")
