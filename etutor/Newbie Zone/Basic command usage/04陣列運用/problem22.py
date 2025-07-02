n = int(input())
text = input()
i = 0
while i < len(text):
    # 取長度n的部分
    line = text[i:i+n]

    # rstrip()用來刪除字串末尾的空白字元
    if line.endswith(" "):
        line = line.rstrip()
        last_space = line.rfind(" ")
        line = line[:last_space] + " " + line[last_space]

    elif i+n < len(text) and text[i+n].isalpha() and text[i+n-1].isalpha():
        line = line[:-1] + "-" # 最後一個字拿掉換成"-"
        i -= 1

    print(line)
    i += n
