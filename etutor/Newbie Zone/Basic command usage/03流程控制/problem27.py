m, n = map(int, input().split())
for i in range(1, m+1):
    for j in range(1, n+1):
        print(f"{i}x{j}={i*j}")
