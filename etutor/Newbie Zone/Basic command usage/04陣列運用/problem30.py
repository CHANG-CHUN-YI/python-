n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# start sort
segments.sort()

merge = []
start, end = segments[0]
for l, r in segments[1:]:
    if l <= end:
        end = max(end, r)
    else:
        merge.append((start, end))
        start, end = l, r
# 最後一段也要加上
merge.append((start, end))
total = sum(r-l for l, r in merge)
print(total)
