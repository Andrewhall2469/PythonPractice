message = input("Enter any message")
find = input("Enter what to find")

def findandcount(message, find):
    i = 0
    count = 0
    while i < len(message):
        if message[i:i+len(find)] == find:
            count = count +1
        i = i + 1
    return count

print(find, "occurs", findandcount(message, find), "times in the sentence")

