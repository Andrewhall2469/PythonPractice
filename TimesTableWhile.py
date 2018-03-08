a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
i = int(input("Enter Increment"))

while a <= b:
    c = 1
    while c<=i:
        print(a,"*",c,"=",a*c)
        c = c + 1
    a = a + 1