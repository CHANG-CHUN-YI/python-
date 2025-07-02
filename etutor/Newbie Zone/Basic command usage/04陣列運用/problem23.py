anomal = [
    "rat", "ox", "tiger", "rabbit", "dragon", "snake",
    "horse", "sheep", "monkey", "rooster", "dog", "pig"
]

year = int(input())
index = (year - 1900) % 12
print(anomal[index])
