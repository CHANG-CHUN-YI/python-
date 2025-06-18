"""
Python預設的round()或f"{:.1f}"使用的是「round half to even」（又叫 Banker's rounding）：
72.25 → 72.2（因為小數部分 .25 被視為靠近偶數 72.2）
"""
from decimal import Decimal, ROUND_HALF_UP

n = int(input())
for i in range(n):
    a = Decimal(input())
    result = a * a
    rounded = result.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    print(f"{rounded}")
