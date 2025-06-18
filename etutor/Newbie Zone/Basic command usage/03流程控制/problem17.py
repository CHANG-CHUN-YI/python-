n = int(input())
for i in range(n):
    x = float(input())
    if x < 18.5:
        print("體重過輕")
    elif 18.5 <= x < 24:
        print("正常")
    elif 24 <= x < 28:
        print("體重過重")
    else:
        print("肥胖")