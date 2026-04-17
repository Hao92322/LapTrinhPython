chieudaiday = float(input("Nhap chieu dai day hinh chu nhat (cm):"))
chieurongday = float(input("Nhap chieu rong day hinh chu nhat (cm):"))
chieucao = float(input("Nhap chieu cao hinh khoi chu nhat (cm):"))
ndigits = int(input("So luong so le can hien thi:"))
dientichday = round(chieudaiday*chieurongday,ndigits)
thetich = round(dientichday * chieucao,ndigits)
print("Dien tich day hinh chu nhat = %scm\u00b2"%(dientichday))
print("The tich hinh khoi = %scm\u00b3"%(thetich))
#print("Hello World")
#ten = 'Ty' #string
#tuoi = 18 #int
#don_gia = 123.45 #float
#PhaiNu = False #boolean
#a,b,c = 1,2,3
#d = 3.21+12j
#print('(%d*%d)+%d = %d'%(a,b,c,(a*b)+c))
#su dung unicode them u
#eval
#map