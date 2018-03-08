names=[]
choice =""

longest_string = [names]

while choice !="quit":
    choice = input("Enter name or enter quit to close program:")
    if choice !="quit":
        names.append(choice)
i=1
longest_string = names[0]
second_highest = names[0]

while i < len(names):
    if len(names[i]) > len(second_highest) and len(names[i]) < len(longest_string):
        second_highest = names[i]
    if len(names[i]) > len(longest_string):
        second_highest = longest_string
        longest_string = names[i]
    i = i + 1

print(longest_string)
print(second_highest)



