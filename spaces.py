message = input("Enter any message")
i = 0
b = 1
while i < len(message):
    a = message[i]
    i = i + 1

    if a == " ":
        b = b + 1

print(b, "words")
