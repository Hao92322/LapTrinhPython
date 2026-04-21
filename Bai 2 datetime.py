from datetime import datetime,timedelta,date
day1 = input("Nhap Ngay thang nam (DD/MM/YYYY): ")
day2 = input("Nhap Ngay thang nam (DD/MM/YYYY): ")
dateformat = "%d/%m/%Y"
try:
    date1 = datetime.strptime(day1,dateformat)
    date2 = datetime.strptime(day2,dateformat)
except ValueError:
    print("Sai dinh dang")
distance = abs((date2 - date1).days) #lay ngay 2 - ngay1 va lay gia tri tuyet doi
print("Khoang cach giua 2 ngay =",distance)


