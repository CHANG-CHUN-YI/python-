# 也可以把矩陣index列出來，兩個for迴圈解決

n, direction = input().split()
n = int(n)

# 建立初始矩陣(二維)
# 外層:for i in range(n)(n列)
# 內層:每列要放n個元素
matrix = [[i * n + j + 1 for j in range(n)]for i in range(n)]

# zip後是tuple，要轉為list
# 順時針
if direction == "R":
    # 先上下翻轉再轉置
    # zip(*)可將矩陣橫的變直的
    matrix = [list(row) for row in zip(*matrix[::-1])]
# 逆時針
elif direction == "L":
    # 先轉置再上下翻轉
    matrix = [list(row) for row in zip(*matrix)]
    matrix = matrix[::-1]
# 上下顛倒
else:
    matrix = matrix[::-1]

for row in matrix:
    print(" ".join(map(str, row)))