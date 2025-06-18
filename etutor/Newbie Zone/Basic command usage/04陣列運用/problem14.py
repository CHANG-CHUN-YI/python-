# 一個子集合，總和s最接近total / 2
# |total - 2s|最小
n = int(input())
weight = list(map(int, input().split()))
total = sum(weight)

# 所有可能的子集合總和
possible = {0}
for w in weight:
    new = set()
    for s in possible:
        new.add(s+w)
    possible = possible.union(new)

# 找最接近total/2的子集和s
half = total//2
min_diff = 200000
for i in possible:
    diff = abs(total - 2*i)
    if diff < min_diff:
        min_diff = diff

print(min_diff)