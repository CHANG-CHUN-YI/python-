import math
a_1, a_2 = map(int,input().split())
b_1, b_2 = map(int,input().split())

ans = math.sqrt((b_1 - a_1)**2 + (b_2 - a_2)**2)
print(f"{ans:.2f}")