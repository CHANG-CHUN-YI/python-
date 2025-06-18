n = int(input())
arr = input().split()  # 一次讀入n組數字
k = input()
num = 0
for item in arr:
    # 檢查k的每個字元是否都在item中出現
    if all(char in item for char in k):
        num += 1
print(num)
