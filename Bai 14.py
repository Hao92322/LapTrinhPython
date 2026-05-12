Money = [1,2,5,10,20,50,100,200,500]
SumMoney = 0
try:
    moneyinput = int(input())
    print(f'X = {moneyinput} : ')
    for i in range(len(Money)-1,0,-1):  
        if moneyinput // Money[i] > 0:
            #Moneytransfer[i]= moneyinput // Money[i]
            SumMoney += moneyinput//Money[i]
            print(f'Loai {Money[i]} gom {moneyinput//Money[i]} to')
        moneyinput = moneyinput % Money[i]
    
    print(f'TONG CONG CO {SumMoney} TO')
except:
    print("Sai dinh dang")
    
    
