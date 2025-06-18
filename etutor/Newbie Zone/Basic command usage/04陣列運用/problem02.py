n = int(input())
p = input()
t = int(input())

group = []
for i in range(0, n, t):
    group.append(p[i:i+t])
print(" ".join(group))
