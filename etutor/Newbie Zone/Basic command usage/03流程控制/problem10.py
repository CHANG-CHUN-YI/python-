n = int(input())
if n%400 == 0 or n%4 == 0 and n%100 != 0:
    print("Bissextile Year")
else:
    print("Common Year")
