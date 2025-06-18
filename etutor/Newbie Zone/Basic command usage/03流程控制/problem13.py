n = int(input())
if n >= 100:
    print("百元 " + str(n // 100))
    n = n % 100
if 10 <= n <= 99:
    print("十元 " + str(n // 10))
    n = n % 10
if n < 10:
    print("壹元 " + str(n))
