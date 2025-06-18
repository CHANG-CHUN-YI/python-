n = input()
digit = list(n) # 拆成字元
total = 0
for i in digit:
    total += int(i)**3
if total == int(n):
    print("YES")
else:
    print("NO")