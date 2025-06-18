n = int(input())
a = list(map(int, input().split()))
b = []
total = 0
for i in range(n):
    total += a[i]
    b.append(total)
print(" ".join(map(str, b)))
