def hellomessage():
    print("hello")
    print("my")
    print("friends")

def addition(A,B):
    C = A + B
    print("The Result is =", C)

def biggestnumber(A,B):
    if A > B:
        print(A,"is bigger")
    if B > A:
        print(B, "is bigger")
    if A == B:
        print(A,"=",B)

print("Welcome to the program!")

D = int(input("Please enter first number for addition"))
C = int(input("Please enter second number for addition"))

E = int(input("Please Enter Your First Number"))
F = int(input("Please Enter Your Second Number"))

hellomessage()
addition(D,C)
biggestnumber(E,F)
