a, b, c = map(int, input().split())
total = a + b + c
if total > 9:
    print(str(total) + " H")
else:
    print(str(total) + " L")