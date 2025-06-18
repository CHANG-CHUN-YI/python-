n = int(input())
for i in range (n):
    x = int(input())
    if 90 <= x <= 100:
        print("優等")
    elif 80 <= x <= 89:
        print("甲等")
    elif 70 <= x <= 79:
        print("乙等")
    elif 60 <= x <= 69:
        print("丙等")
    else:
        print("不及格")