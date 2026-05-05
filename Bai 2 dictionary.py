from collections import Counter
s1 = input("Nhap chuoi s1 :")
s2 = input("Nhap chuoi s2 :")
dict1 = Counter(s1)
dict2 = Counter(s2)
#Cau a
res = dict1&dict2
print("Cac chu cai xuat hien trong ca 2 chuoi : ",end="")
for k in res:
    print(k,end=" ")
print()
#Cau B
resB = dict1-dict2
resB2 = dict2-dict1
print("So ky tu co trong s1 nhung ko co trong s2 = ",end="")
print(len(resB))
print("So ky tu co trong s2 nhung ko co trong s1 = ",end="")
print(len(resB2))
#Cau C
print("Nhung ky tu xuat hien trong s1 nhung khong xuat hien trong s2 :",end="")
for k in resB:
    print(k,end=" ")
print("\nNhung ky tu xuat hien trong s2 nhung khong xuat hien trong s1 :",end="")
for k in resB2:
    print(k,end=" ")
