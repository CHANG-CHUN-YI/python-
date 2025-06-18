def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1,1):
        if n % i == 0:
            return False
    return True


n = input()
max_prime = 0

for i in range(len(n)):
    for j in range(i+1, len(n)+1):
        num = int(n[i:j])
        if prime(num):
            max_prime = max(max_prime, num)

if max_prime != 0:
    print(max_prime)
else:
    print("No prime found")
