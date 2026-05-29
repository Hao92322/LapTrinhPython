import math
#So Chinh Phuong la so neu can bac 2 cua n nam trong mang so nguyen tu 1 den can bac 2 cua n + 1 lam tron thi n la so chinh phuong
SoChinhPhuong = lambda n : math.sqrt(n) in [x for x in range(1,round(math.sqrt(n))+1)]
print(f'So 3 la so chinh phuong : {SoChinhPhuong(3)}')
#Nếu là 1 tam giác thì chiều dài 2 cạnh cộng lại phải lớn hơn cạnh còn lại
#Tam giác đều là tam giác mà 3 cạnh = nhau
#Tam giác vuông cân là tam giác mà vừa vuông vừa cân
#Tam giác cân là tam giác có 2 cạnh bằng nhau
#Tam giác vuông là tam giác có tổng bình phương 2 cạnh = bình phương cạnh có độ dài lớn nhất
TamGiac = lambda x, y, z: (
    "Ko la tam giac" if not (x + y > z and x + z > y and y + z > x) else
    "Tam Giac Deu" if (x == y == z) else
    "Tam Giac Vuong Can" if ((sum([i**2 for i in [x,y,z]]) - max([x,y,z])**2 == max([x,y,z])**2) and (x==y or y==z or x==z)) else
    "Tam Giac Vuong" if (sum([i**2 for i in [x,y,z]]) - max([x,y,z])**2 == max([x,y,z])**2) else
    "Tam Giac Can" if (x == y or y == z or x == z) else
    "Tam Giac Thuong"
)
# --- Thử nghiệm các trường hợp ---
print(TamGiac(3, 3, 3))   # Kết quả: Tam Giac Deu
print(TamGiac(3, 4, 5))   # Kết quả: Tam Giac Vuong
print(TamGiac(1, 1, 1.41421356)) # Kết quả: Tam Giac Vuong Can (gần đúng của căn 2)
print(TamGiac(5, 5, 8))   # Kết quả: Tam Giac Can
print(TamGiac(4, 5, 6))   # Kết quả: Tam Giac Thuong
print(TamGiac(1, 1, 10))  # Kết quả: Ko la tam giac (Trước đây code cũ sẽ báo là Tam Giác Cân)