m, n = input().split()
sum = 0
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        text = n[i:j]
        if m == text:
            sum += 1

print(sum)
