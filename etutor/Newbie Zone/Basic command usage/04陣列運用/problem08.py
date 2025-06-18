n = int(input())
a = list(map(int, input().split()))
c = []
for i in range(n):
    b = list(map(int, input().split()))
    for num in b:
        if num in a and num not in c:
            c.append(num)
print(len(c))
