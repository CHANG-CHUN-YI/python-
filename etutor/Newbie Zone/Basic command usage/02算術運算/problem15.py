num = int(input())
if num <= 800:
    print(f"{num*0.9:.1f}")
elif 800 < num < 1500:
    print(f"{num * 0.9 * 0.9:.1f}")
else:
    print(f"{num * 0.9 * 0.79:.1f}")