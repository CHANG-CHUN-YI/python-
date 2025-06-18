n = int(input())
total = 0
max = 0
up_90 = 0
up_600 = 0
for i in range(n):
    x = int(input())
    total += x
    if x >= 900:
        up_90 += 1
    elif 600 <= x <= 700:
        up_600 += 1
    if max < x:
        max = x
print(max)
print(up_90)
print(up_600)
print(f"{total/n:.1f}")
