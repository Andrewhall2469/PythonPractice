alpha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

message = input("Enter any message:")
i=0
while i < len(message):
    char=message[i]
    if ord(char) >= 65 and ord(char)<=90:
        alpha[ord(char)-65]+=1
    if ord(char) >= 97 and ord(char) <= 122:
        alpha[ord(char)-97]+=1
    i=i+1

i = 0

while i <= 25:
    if alpha[i] != 0:
        print(chr(i+65),"=", alpha[i])
    i = i +1