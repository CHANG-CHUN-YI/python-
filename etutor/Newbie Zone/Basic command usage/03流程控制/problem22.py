# (x−h)^2 + (y-k)^2 < r^2
# 圓心座標為 (h,k) 半徑為 r 點座標為 (x,y)

x, y = map(int, input().split())
if x**2 + y**2 < 10000:
    print("inside")
else:
    print("outside")
