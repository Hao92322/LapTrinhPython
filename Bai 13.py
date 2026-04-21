import re

def chuan_hoa_va_dem(chuoi):
    # cat khoang trang thua dau va cuoi chuoi
    chuoi = chuoi.strip()
    # xu ly cho dau cham dau phay sat vao tu
    chuoi = re.sub(r'\s+([.,])', r'\1', chuoi)
     # cat khoang trang giua cac tu
    chuoi = re.sub(r'\s+', ' ', chuoi)
    
    print(f"--- Chuỗi sau khi chuẩn hóa: '{chuoi}' ---")
    

van_ban = input("Nhập vào chuỗi: ")
chuan_hoa_va_dem(van_ban)