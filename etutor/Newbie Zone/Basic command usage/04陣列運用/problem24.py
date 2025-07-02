n = int(input())
w = [list(map(int, input().split())) for i in range(n)]

edges = []
for i in range(n):
    for j in range(n):
        edges.append((w[i][j], i, j)) # score,man,woman
edges.sort(reverse=True) # 依照好感度(大到小)

used_man = set()
used_woman = set()
match = []
for score, man, woman in edges:
    if man not in used_man and woman not in used_woman:
        used_man.add(man)
        used_woman.add(woman)
        match.append((man+1, woman+1)) #輸出從1開始

for i, j in match:
    print(f"boy {i} pair with girl {j}")