n = int(input())
max_sc = 0
min_sc = 100
average = 0
pass_num = 0
for i in range(n):
    b = int(input())
    if b > max_sc:
        max_sc = b
    if b < min_sc:
        min_sc = b
    if b >= 60:
        pass_num += 1
    average += b

print("Max:" + str(max_sc))
print("Min:" + str(min_sc))
print(f"Average:{average/n:.1f}")
print("Pass:" + str(pass_num))
