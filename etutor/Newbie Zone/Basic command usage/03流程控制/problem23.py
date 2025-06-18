a, b, c = map(int, input().split())
order = input()

s_to_b = sorted([a, b, c])
a = str(s_to_b[0])
b = str(s_to_b[1])
c = str(s_to_b[2])

if order == 'Asc':
    print(a + "<" + b + "<" + c)
else:
    print(c + ">" + b + ">" + a)
