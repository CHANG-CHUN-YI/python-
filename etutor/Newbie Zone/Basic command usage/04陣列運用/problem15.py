a = list(map(int, input().split()))
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1

for j in b:
    if b[j] == 2:
        print(j)
