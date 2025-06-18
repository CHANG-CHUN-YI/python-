# 最大除數是開根號後的整數，假如都沒有可以整除的就是質數
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

num = int(input())
for i in range(num-1,1,-1):
    if is_prime(i):
        print(i)
        break