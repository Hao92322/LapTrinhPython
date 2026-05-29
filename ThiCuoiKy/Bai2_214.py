import math

# 1. Hàm kiểm tra số nguyên tố (bắt đầu chạy từ 2 đến phần nguyên căn bậc hai của n)
SoNT = lambda n : n > 1 and len([x for x in range(2, int(math.sqrt(n)) + 1) if n % x == 0]) == 0
print(f'So 17 la so nguyen to : {SoNT(17)}')

# 2. Hàm đếm các số nguyên tố nhỏ hơn n
SoluongSoNTNhoHonN = lambda n : len([x for x in range(n) if SoNT(x)])
print(f'So luong so nguyen to nho hon 100 = {SoluongSoNTNhoHonN(100)}')

# 3. Hàm liệt ke số nguyên tố là ước số của n (thêm điều kiện n % x == 0)
DanhSachUocSoLaSoNT = lambda n : [x for x in range(2, n + 1) if n % x == 0 and SoNT(x)]

# Kiểm tra kết quả với n = 36
print(f'Danh sach cac uoc so cua 36 la so nguyen to : {DanhSachUocSoLaSoNT(36)}')