a = input().replace(",", "")
max_num = "".join(sorted(a, reverse = True))
min_num = "".join(sorted(a))
print(int(max_num)-int(min_num))
