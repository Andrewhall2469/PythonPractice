message = input("Please enter any message")
lower = 0
upper = 0
digit = 0
i = 0

while i < len(message):
    char = message[i]

    if ord(char) >= 65 and ord(char) <= 90:
        upper = upper + 1

    if ord(char) >= 97 and ord(char) <= 122:
        lower = lower + 1

    if ord(char) >= 48 and ord(char) <= 57:
        digit = digit + 1
    i = i + 1

print("The number of uppercase letters used was", upper)
print("The number of lowercase letters used was", lower)
print("The number of digits used was", digit)