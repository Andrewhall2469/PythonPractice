# Ask the user to input 10 numbers and print the largest odd number
a = input('Enter a value: ')
b = input('Enter a value: ')
c = input('Enter a value: ')
d = input('Enter a value: ')
e = input('Enter a value: ')
f = input('Enter a value: ')
g = input('Enter a value: ')

list1 = [a, b, c, d, e, f, g]
list2 = []  # used to sort the ODD values into
list3 = (a+b+c+d+e+f+g)     # use this because all 10 values could have used value '3'
                            # and had the total vaplue become an even number

if list3 % 2 == 0:    # does list 3 mod 2 have no remainder
    if a % 2 == 0:    # and if so then by checking if 'a' has an even value
                        # it rules out the possibility of all values having an odd value entered
        print('All declared variables have even values')
    else:
        for odd in list1:   # for loop to loop through and pick out odd values
            if odd % 2 == 1:  #if each value tested has a remainder of one to mod 2
                list2.append(odd)   # then append that value into list 2
        odd = str(max(list2))   #created the variable odd for the highest ODD value from
                                # list to to concatenate it with a string
        print ('the largest ODD value is ' + odd)
