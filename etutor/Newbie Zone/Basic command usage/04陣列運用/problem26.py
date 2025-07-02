r, c = map(int, input().split())
matrix = []
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = list(zip(*matrix))

for row in transpose:
    print(" ".join(map(str, row)))
