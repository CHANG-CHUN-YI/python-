n = int(input())
y = 0
for i in range(n):
    x = int(input())
    if x > y:
        y = x
print(y)
