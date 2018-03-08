def add(A, B):
    C = A + B
    return C


D = int(input("Enter a value"))
E = int(input("Enter another value"))

print(D, E)
if add(D,E) > 30:
    print("Good")
else: print("Bad")
