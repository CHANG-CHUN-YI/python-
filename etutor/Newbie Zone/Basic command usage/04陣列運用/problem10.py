n = int(input())
coins = list(map(int, input().split()))
money = int(input())

# dp[i]:湊出金額i的所有組合，每個組合是list
# 記錄每種硬幣用了幾個
dp = [[]for i in range(money+1)]
dp[0] = [[0]*n]

for i in range(n):
    coin = coins[i]
    for j in range(coin,money+1):
        for way in dp[j - coin]:
            new = way.copy()
            new[i] += 1 # 在這個組合中，第i種硬幣多用1個
            dp[j].append(new)

# 小到大
dp[money].sort()
for way in dp[money]:
    print(f"({','.join(map(str, way))})")
