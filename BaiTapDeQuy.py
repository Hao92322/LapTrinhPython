#1
def TongChuSo(n):
    if(n//10 == 0):
        return n
    return TongChuSo(n//10) + n%10
#2
def GiaiThua(n):
    if(n==1):
        return 1
    return GiaiThua(n-1)*n
#3
def LuyThua(a,b):
    if(b == 0):
        return 1
    if(b == 1):
        return a
    return LuyThua(a,b-1)*a
#4
def UCLN(a,b):
    if(b == 0):
       return a
    return UCLN(b,a%b) # a va b chia het cho uoc chung lon nhat thi a%b cung chia het cho uoc chung lon nhat
#5
def Fibonaci(n):
    if(n<=2):
        return 1
    return Fibonaci(n-2) + Fibonaci(n-1)
