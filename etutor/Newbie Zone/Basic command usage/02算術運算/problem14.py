# 無條件進位 #
import math
num = int(input())
other = 30 * 2.54
me = 100
ans = (num * 100) / (me - other)
print(math.ceil(ans))
