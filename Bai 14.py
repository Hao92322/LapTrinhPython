Money = [1,2,5,10,20,50,100,200,500]
Moneytranfer = [0]*10
try:
    moneyinput = int(input())
    print(f'X = {moneyinput} : ')
    while moneyinput > 0:
        for i in range(len(Money)-1,0,-1):  
            if moneyinput // Money[i] > 0:
                Moneytranfer[i]= moneyinput // Money[i]
            moneyinput = moneyinput % Money[i]
    for i in range(len(Moneytranfer)-1,0,-1):
        if Moneytranfer[i] > 0:
            print(f'Loai {Money[i]} gom {Moneytranfer[i]} to')
    print(f'TONG CONG CO {sum(Moneytranfer)} TO')
except:
    print("Sai dinh dang")
    
    
