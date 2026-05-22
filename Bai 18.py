import math
#Cau a So than thien
Sothanthien = lambda n : math.gcd(n,int(str(n)[::-1])) == 1
#Cau b So Chinh Phuong
SoChinhPhuong = lambda n : math.sqrt(n) in [x for x in range(1,round(math.sqrt(n))+1)]
#Cau c So dong nhat
SoDongNhat = lambda n : n>0 and all(y == str(n)[0] for y in [x for x in str(n)])
#Cau d So Hoan Thien
SoHoanThien = lambda n : n == sum([x for x in range(1,n//2+1) if n%x == 0])
#Cau e So phong phu
SoPhongPhu = lambda n : n < sum([x for x in range(1,n//2+1) if n%x == 0])
#Cau f So Tang Dan
SoTangDan =  lambda n : [int(x) for x in str(n)] == sorted([int(x) for x in str(n)])
#Cau g So Armstrong
SoArmStrong = lambda n : n == sum([int(x)**len(str(n)) for x in str(n)])
#Cau h So nguyen to
#Cach 1 co 2 uoc so la 1 va n 
SoNguyenToC1 = lambda n : len([x for x in range(1,n+1) if n%x == 0]) == 2
#Cach 2 tinh tong uoc so
SoNguyenToC2 = lambda n : sum([x for x in range(1,n+1) if n%x == 0]) == n+1
#Cach 3 n <= 1 hoac n chia chan cho 2 den can bac 2 cua n thi n ko phai la so nguyen to
SoNguyenToC3 = lambda n : n>=1 and len([x for x in range(2,round(math.sqrt(n))+1) if n%x == 0]) == 0
#Cach 4
#Cau i So Palindrome
SoPalindrome = lambda n : n == int(str(n)[::-1])
#Cau j So nguyen to Palindrome
SoNguyenToPalindrome = lambda n : n == int(str(n)[::-1]) and n>=1 and len([x for x in range(2,round(math.sqrt(n))+1) if n%x == 0]) == 0
#Cau k So loc phat
#Cach 1 Su dung all
SoLocPhatC1 = lambda n : all(y in [6,8] for y in [int(x) for x in str(n)])
#Cach 2 dem so luong phan tu 6 va 8 roi + lai = len(n) thi la so loc phat
SoLocPhatC2 = lambda n : len([x for x in str(n) if x in ['6','8']]) == len(str(n))
#Cau l So loc phat palindrome
SoLocPhatPalindrome = lambda n : SoPalindrome(n) and SoLocPhatC2(n)

def InSoTheoLambda(ld):
    for i in range(1,10**3):
        if(ld(i)):
            print(i)
#Huong dan su dung test ham nao thi go comment ham do
#InSoTheoLambda(Sothanthien)
# InSoTheoLambda(SoChinhPhuong)
InSoTheoLambda(SoDongNhat)
# InSoTheoLambda(SoHoanThien)
# InSoTheoLambda(SoPhongPhu)
# InSoTheoLambda(SoTangDan)
# InSoTheoLambda(SoArmStrong)
# InSoTheoLambda(SoNguyenToC1)
# InSoTheoLambda(SoPalindrome)
# InSoTheoLambda(SoNguyenToPalindrome)
# InSoTheoLambda(SoLocPhatC2)
# InSoTheoLambda(SoLocPhatPalindrome)