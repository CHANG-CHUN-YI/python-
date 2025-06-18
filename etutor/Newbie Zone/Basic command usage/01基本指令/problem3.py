# 用reversed
# 或是 num[::-1]
"""
    num[start:stop:step]
    start:起始索引（包含）
    stop:結束索引（不包含）
    step:每次移動的步長

    '分隔符'.join(可迭代物件)
    join() 的前面必須是字串（作為分隔符），後面要是一個每個元素都是字串的可迭代物件（如列表或字串）。
"""

num = input()
print(','.join(num[::-1]))
