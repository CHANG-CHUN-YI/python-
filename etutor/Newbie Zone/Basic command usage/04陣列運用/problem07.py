n = int(input())
a = list(map(int, input().split()))
total_1 = 0
total_2 = 0
sum = 0
for i in range(n):
    total_1 += a[i]
    total_2 += a[n-1-i]
    if total_1 == total_2:
        sum += 1
print(sum)
