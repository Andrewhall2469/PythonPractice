message = input("Enter any message")
i = 0
b = 0


while i < len(message):
    a = message[i]

    if a == " ":
        print(message[b:i])
        b = i + 1
    if i == len(message) - 1:
        print(message[b:i+1])


    # if a == " ":
    #     print("")
    # else:
    #     print(a, end="")
    # i = i + 1
