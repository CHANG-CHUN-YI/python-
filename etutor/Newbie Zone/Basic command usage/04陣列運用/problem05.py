n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(n-1):
    b.append(a[i+1]-a[i])
print(" ".join(map(str, b)))
