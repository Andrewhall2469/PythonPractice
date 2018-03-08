message = input("Enter any message")
i = len(message) -1
word = ""

while i >= 0:

    if message[i] == " ":
        print(word)
        word=""
    else:
        word = message[i] + word
    i = i - 1
print(word)