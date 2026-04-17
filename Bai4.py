n = int(input("Nhap n :"))
sole = 0
sochan = 0
while n>0:
    digit = n%10
    if(digit % 2 != 0):
        sole=sole+1
    else:
        sochan=sochan+1
    n=n//10
print("so luong so le = %d" %(sole))
print("so luong so chan = %d" %(sochan))

