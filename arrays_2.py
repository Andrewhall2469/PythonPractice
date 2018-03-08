names=[]
choice =""

longest_len = 0
longest_string = []

while choice !="quit":
    choice = input("Enter name or enter quit to close program:")
    if choice !="quit":
        names.append(choice)


i=0

while i < len(names):
    # print((i+1),".",names[i])
    longest_string = (max(names, key=len))
    print(longest_string)

    i = i + 1
else:
    i = i + 1