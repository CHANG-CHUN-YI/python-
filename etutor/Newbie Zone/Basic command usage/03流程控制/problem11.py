n = int(input())
for i in range(n):
    x = int(input())
    if 0 <= x <= 60:
        if x > 37:
            print("避免外出")
        else:
            print("可依需要待在戶外")
    elif 70 <= x <= 500:
        if x > 150:
            print("避免外出")
        else:
            print("可依需要待在戶外")
