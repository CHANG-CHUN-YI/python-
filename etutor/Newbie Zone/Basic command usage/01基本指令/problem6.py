# input().split() 會把輸入依空格切開，回傳列表
num_1, num_2 = input().split()
for j in range(int(num_2)):
    print('*' * int(num_1))
