def UCLN(a,b):
    if b==0:
        return a
    return UCLN(b,a%b)
def LaSoThanThien(num):
    rvnum = int(str(num)[::-1])
    ucln = UCLN(num,rvnum)
    if ucln == 1:
        return True
    return False
    
def InSoThanThien(a,b):
    for i in range(a,b):
        if LaSoThanThien(i) == True:
            print(i)
a = int(input("Nhap vao so a:"))
b = int(input("Nhap vao so b:"))
InSoThanThien(a,b)