#Lay chieu dai va chieu rong duoc nhap tu ban phim
try:
    chieudaiday = float(input("Nhap chieu dai day hinh chu nhat (cm):"))
    chieurongday = float(input("Nhap chieu rong day hinh chu nhat (cm):"))
    chieucao = float(input("Nhap chieu cao hinh khoi chu nhat (cm):"))
    ndigits = int(input("So luong so le can hien thi:"))
    dientichday = round(chieudaiday*chieurongday,ndigits)
    thetich = round(dientichday * chieucao,ndigits)
    print("Dien tich day hinh chu nhat = %scm\u00b2"%(dientichday))
    print("The tich hinh khoi = %scm\u00b3"%(thetich))
except ValueError:
    print("Sai dinh dang.!!")
