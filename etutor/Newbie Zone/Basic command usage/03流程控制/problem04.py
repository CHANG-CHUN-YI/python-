n = int(input())
sub = {}
# 紀錄是否有過半
j = 0
for i in range(n):
    obj, score = input().split()
    score = int(score)
    sub[obj] = score
for obj in sub:
    if sub[obj] > 60:
        print(obj)
        j += 1
if n/2 <= j:
    print("晉級")
else:
    print("失敗")