#cipher tex co dang #-soluong-kytu
def decode_cipher(cipher_text: str) -> str:
    result = []
    i = 0
    n = len(cipher_text)

    while i < n:
        if cipher_text[i] == '#':
            # Lấy số lần lặp (1 chữ số theo đề bài)
            count = int(cipher_text[i + 1])
            char = cipher_text[i + 2]
            result.append(char * count)
            i += 3
        else:
            result.append(cipher_text[i])
            i += 1

    return ''.join(result)

string = input("Nhap chuoi cua ban: ")
print(decode_cipher(string))
            
            