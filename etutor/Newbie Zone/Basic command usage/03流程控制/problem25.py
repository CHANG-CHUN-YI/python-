s = int(input())
n = int(input())
total = 0
for i in range(n):
    total += s
    s = s*2
print("第" + str(n) + "天共存" + str(total) + "元")
