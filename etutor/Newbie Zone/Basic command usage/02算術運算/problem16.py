h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())
total = (h2-h1)*60 + (m2-m1)
sum = 0
if 0 < total <= 120:
    sum = int(total/30)*30
    print(sum)
elif 120 < total <= 240:
    sum = 120 + int((total-120)/30)*40
    print(sum)
else:
    sum = 120 + 160 + int((total-240)/30)*60
    print(sum)