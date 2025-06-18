morse_code = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
    "....", "..", ".---", "-.-", ".-..", "--", "-.",
    "---", ".--.", "--.-", ".-.", "...", "-", "..-",
    "...-", ".--", "-..-", "-.--", "--.."
]

dic = dict(zip(morse_code, "abcdefghijklmnopqrstuvwxyz"))

a = input().split()
b = ""
for i in a:
    if i in dic:
        b += dic[i]

print(b.upper())