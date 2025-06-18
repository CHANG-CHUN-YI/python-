num = int(input())
days = num//86400;
num = num - 86400 * days

hours = num // 3600
num = num - hours * 3600

minutes = num // 60
seconds = num - minutes*60

print(str(days) + " days")
print(str(hours) + " hours")
print(str(minutes) + " minutes")
print(str(seconds) + " seconds")