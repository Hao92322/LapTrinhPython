import math
#So chinh phuong la so co can bac 2 la so nguyen logic ham em da giai thich o bai 3
SoChinhPhuong = lambda n : math.sqrt(n) in [x for x in range(1,round(math.sqrt(n))+1)]
#In ra ko su dung user defined
print([x for x in range(1,10**4) if SoChinhPhuong(x)])
#So hoan thien la so ma co tong cac uoc so = chinh no
SoHoanThien = lambda n : n == sum([x for x in range(1,n//2+1) if n%x == 0])
#In ra so hoan thien tu 1 - 10000
print([x for x in range(1,10**4) if SoHoanThien(x)])