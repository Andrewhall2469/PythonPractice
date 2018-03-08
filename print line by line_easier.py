message = input("Enter any message")
i = 0
word = ""

while i < len(message):
    if message[i]==" ":
        print(word)
        word=""
    else:
        word = word + message[i]

    i=i+1

print(word)