a, b, c = map(int, input().split())
# 小到大排序
sides = sorted([a, b, c])
a = sides[0]
b = sides[1]
c = sides[2]
if a + b <= c:
    print("Not Triangle")
else:
    if a**2 + b**2 == c**2:
        print("Right Triangle")
    elif a**2 + b**2 < c**2:
        print("Obtuse Triangle")
    elif a**2 + b**2 > c**2:
        print("Acute Triangle")
    else:
        print("Not Triangle")
