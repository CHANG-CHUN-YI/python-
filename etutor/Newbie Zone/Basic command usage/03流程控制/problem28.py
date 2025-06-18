n = int(input())


def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1, 1):
        if x % i == 0:
            return False
    return True


if n%2 == 0 and prime(n) == True:
    print("even prime")
elif n%2 != 0 and prime(n) == True:
    print("odd prime")
elif n % 2 == 0 and prime(n) == False:
    print("even")
elif n%2 != 0 and prime(n) == False:
    print("odd")
