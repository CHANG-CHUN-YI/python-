n = int(input())
b = []
for i in range(n):
    x = int(input())
    b.append(x)
b.sort(reverse=True)
print("".join(map(str, b)))
