n = int(input())

a = list(map(int, input().split()))

x = int(input())
a.append(x)

a.sort()
print(",".join(map(str, a)))
