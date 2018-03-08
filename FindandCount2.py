message = input("Enter any message")
find = input("Enter part of message to find")

def FindandCount(message, find):
    count = 0
    i = 0
    while i < len(message):
        if message[i:i+len(find)] == find:
            i += len(find)
            count = count + 1
        else:
            i = i + 1
    return count

print(find, "appears", FindandCount(message, find), "times in the sentence")