num = int(input())
if num < 10:
    print(int(num*100))
elif 10 <= num < 30:
    print(int(num*100*0.9))
elif 30 <= num <= 99:
    print(int(num * 100 * 0.8))
else:
    print(int(num * 100 * 0.7))