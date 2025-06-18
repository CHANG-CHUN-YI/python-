n = input()
try:
    int(n)
    print("int")
except ValueError:
    try:
        float(n)
        print("float")
    except ValueError:
        if len(n) == 1:
            print("char")
        else:
            print("string")
