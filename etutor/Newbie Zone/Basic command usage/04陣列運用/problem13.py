x = int(input())
c = 0
e = 0
m = 0

for i in range(x):
    b = list(map(int, input().split()))
    c += int(b[0])
    e += int(b[1])
    m += int(b[2])

c_aver = float(c/x)
e_aver = float(e/x)
m_aver = float(m/x)
total_aver = (c_aver + e_aver + m_aver)/3

print(f"{total_aver:.1f} {c_aver:.1f} {e_aver:.1f} {m_aver:.1f}")