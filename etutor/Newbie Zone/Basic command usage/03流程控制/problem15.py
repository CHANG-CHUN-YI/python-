n = int(input())
count = 0
num = 2
result = []
total = 0


def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1, 1):
        if x % i == 0:
            return False
    return True


while count < n:
    if prime(num):
        total += num
        result.append(str(num))
        count += 1
    num += 1

print(','.join(result))
print(total)

