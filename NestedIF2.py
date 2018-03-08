num = int(input("Enter the number"))
if num > 7000:
    print("A")
    if num > 9000:
        print("C")
        if num < 10000:
            print("D")
        else:
            print("E")
else:
    print("1")
    if num > 5000:
        print("2")
    else:
        print("3")
        if num > 200:
            print("4")
        else:
            print("5")