#Bai 3 nhap so dien thoai
phone = input()
try:
    setofnum = {int(phone[0])}
    set0_9 = {x for x in range(0,10)}
    for num in phone:
        setofnum.add(int(num))
    print(set0_9.difference(setofnum))
except Exception:
    print("Sai dinh dang")
#bai 4
s = input()
listOfs = list(s.split())
setOfChar = list(set(s.split()))
#neu ko co phan tu bi lap thi in ra None
if(len(listOfs) - len(setOfChar) == 0):
    print("None")
else:
    #(len(listOfs) - len(setOfChar)) so phan tu bi lap lai
    print(listOfs[len(listOfs)-(len(listOfs) - len(setOfChar))])
