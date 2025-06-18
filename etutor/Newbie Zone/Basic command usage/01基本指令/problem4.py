# 原始字典：英文 -> 中文
animal = {"dog": "狗", "cat": "貓", "duck": "鴨", "cow": "牛", "fox": "狐"}
# 產生相反方向的字典：英文 -> 中文
reverse_animal = {v: k for k, v in animal.items()}

name = input()

if name in animal:
    print(animal[name])
else:
    print(reverse_animal[name])
