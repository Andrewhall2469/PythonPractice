num = int(input("Enter any number"))
if num >= 1000:
    print("A")
    if num > 5000:
        print("C")
    else:
        print("E")
else:
    print("B")
    if num > 500:
        print("D")
