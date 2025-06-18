n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
total = 0
for i in range(b, c+1):
    total += a[i-1]
print(total)
