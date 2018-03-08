# prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

#Print out only odd numbers
for x in range(10):
    # check if x is even
    if x % 2 ==0:
        continue
    print(x)
