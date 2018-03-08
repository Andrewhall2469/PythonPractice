message = input("Enter a message")
i=0
word = ""

while i <len(message):

    char = message[i]

    if ord(char) >= 65 and ord(char) <=90:
        word = word + (chr(ord(char) + 32))

    elif ord(char) >= 97 and ord(char) <=122:
        word = word + (chr(ord(char) - 32))

    elif ord(char)  >= 48 and ord(char) <= 57:
        digit = str(int(char) * 2)
        word = word + digit
    else:
        word = word + char
    i=i+1
print(word)
