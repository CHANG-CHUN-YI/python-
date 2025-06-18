# ** 次方
num = int(input())
for i in range(num):
    a = int(input())
    if a > 31:
        print("Value of more than 31")
    else:
        print(2 ** a)
