n = int(input())
sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_5 = 0
for i in range(n):
    x = int(input())
    if 90 <= x <= 100:
        sum_1 += 1
    elif 80 <= x <= 89:
        sum_2 += 1
    elif 70 <= x <= 79:
        sum_3 += 1
    elif 60 <= x <= 69:
        sum_4 += 1
    else:
        sum_5 += 1

print("優等 " + str(sum_1))
print("甲等 " + str(sum_2))
print("乙等 " + str(sum_3))
print("丙等 " + str(sum_4))
print("不及格 " + str(sum_5))
