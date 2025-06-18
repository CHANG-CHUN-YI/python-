# 用queue記錄每輛車的結束時間
# 如果有一輛車已經結束，就重用這輛車
import heapq
n = int(input())
tasks = []

for i in range(n):
    start, end = map(int, input().split())
    tasks.append((start, end))

# 依照開始時間排序
tasks.sort()
# 記錄每輛車的結束時間
heap = []

for start, end in tasks:
    if heap and heap[0] <= start:
        heapq.heappop(heap) # 重用一輛車
    # 加入後會自動調整順序，讓最小的數字變成heap[0]
    heapq.heappush(heap, end) # new car

print(len(heap))
