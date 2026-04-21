from datetime import date,datetime
x = date.today()
Today = datetime.now()
tuantrongthang = int(Today.strftime("%d"))//7#7 ngay la 1 tuan vay lay ngay / 7 la ra tuan trong thang
print("Nam hien tai :",Today.strftime("%Y"))
print("Thang hien tai bang chu : ",Today.strftime("%B"))
print("Tuan hien tai la tuan thu may trong nam :",Today.strftime("%U"))
print("Tuan hien tai la tuan thu may trong thang :",tuantrongthang)
print("Ngay hien tai la ngay thu may trong nam: ",Today.strftime("%j"))
print("Ngay duong lich hien tai la ngay: ",Today.strftime("%d"))
print("Thu cua ngay hien tai: ",Today.strftime("%A"))
print("Gio phut hien tai: ",Today.strftime("%X"))