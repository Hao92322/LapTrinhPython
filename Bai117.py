n = input().strip()
S = 0

# Duyệt tất cả "số con"
for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        sub = int(n[i:j])
        S += sub ** 2

print(S)