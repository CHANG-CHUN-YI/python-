n = int(input())
result = []
for i in range(n+1):
    if i % 2 == 1:
        result.append(str(i))
print(" ".join(result))
