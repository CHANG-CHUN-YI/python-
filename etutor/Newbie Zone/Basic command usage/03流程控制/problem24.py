n = int(input())
for i in range(n):
    total = 1
    x = int(input())
    for j in range(x):
        total *= (j+1)
    print(total)
