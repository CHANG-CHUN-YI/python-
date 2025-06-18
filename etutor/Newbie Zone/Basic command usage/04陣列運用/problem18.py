import string

text = input()
# 初始化a-z等於0
num = {ch: 0 for ch in string.ascii_lowercase}
for ch in text.lower():
    if ch in num:
        num[ch] += 1

print(" ".join(str(num[ch]) for ch in string.ascii_lowercase))
