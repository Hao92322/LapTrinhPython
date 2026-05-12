def MoneyTransfer(moneyinput):
    Money = [1,2,5,10,20,50,100,200,500]
    SumMoney = 0
    print(f'So tien {moneyinput} dong duoc doi thanh: ')
    for i in range(len(Money)-1,0,-1):  
        if moneyinput // Money[i] > 0:
            #Moneytransfer[i]= moneyinput // Money[i]
            SumMoney += moneyinput//Money[i]
            print(f'Loai {Money[i]} gom {moneyinput//Money[i]} to')
        moneyinput = moneyinput % Money[i]
    print(f'TONG CONG CO {SumMoney} TO')
#Bai 20
try:
    money = int(input())
    MoneyTransfer(money)
except:
    print("Sai dinh dang")
#Bai 20 Mo rong
try:
    a = int(input())
    b = int(input())
    if a > b:
        print(f'So tien con thieu {a-b} dong')
    else:
        if a < b:
            #Tien tra lon hon tien hang
            print(f'Ban da tra thua {b-a} dong')
            MoneyTransfer(b-a)
        print("Cam on quy khach !! Hen gap lai !!")
except:
    print("Sai dinh dang")
        
    
    
