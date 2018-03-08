message = input("Enter any message")
i = 0
while i <= len(message):
    print(message[i::-1])
    i = i + 1
    break