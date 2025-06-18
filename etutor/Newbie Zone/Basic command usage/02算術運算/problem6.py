# map函數一次轉型
num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    ans = (a + b) * (a + b)
    print(ans)
