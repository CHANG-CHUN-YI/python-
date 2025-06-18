num_1, num_2 = map(int, input().split())
sum = 0
if 0 < num_1 <= 60:
    sum = num_1 * num_2
    print(f"{sum:.1f}")
elif 61 <= num_1 <= 120:
    sum = (num_1-60) * num_2 * 1.33 + 60 * num_2
    print(f"{sum:.1f}")
else:
    sum = 60 * num_2 + 60 * num_2 * 1.33 + (num_1 - 120) * num_2 * 1.66
    print(f"{sum:.1f}")