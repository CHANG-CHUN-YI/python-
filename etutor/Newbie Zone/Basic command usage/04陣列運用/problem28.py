n, d = input().split(",")
d = int(d)
keep = len(n) - d  # 要保留的字元數

stack = []
for value in n:
    # stack最後一位比現在的大就刪掉
    while d > 0 and stack and stack[-1] > value:
        stack.pop()
        d -= 1
    stack.append(value)
# 因為stack裡面可能還有多餘的數，取到keep
print("".join(map(str, stack[:keep])))
