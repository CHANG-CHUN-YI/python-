# 等差數列公式
# 梯形公式
num = int(input())
for i in range(num):
    a, b = map(int,input().split())
    ans = int((a+b)*(abs(b-a)+1)/2)
    print(ans)