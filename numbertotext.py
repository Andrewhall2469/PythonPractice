def ones(num):
    if num == 1:
        word = " One"
    if num == 2:
        word = " Two"
    if num == 3:
        word = " Three"
    if num == 4:
        word = " Four"
    if num == 5:
        word = " Five"
    if num == 6:
        word = " Six"
    if num == 7:
        word = " Seven"
    if num == 8:
        word = " Eight"
    if num == 9:
        word = " Nine"
    if num == 10:
        word = " Ten"
    if num == 11:
        word = " Eleven"
    if num == 12:
        word = " Twelve"
    if num == 13:
        word = " Thirteen"
    if num == 14:
        word = " Fourteen"
    if num == 15:
        word = " Fifteen"
    if num == 16:
        word = " Sixteen"
    if num == 17:
        word = " Seventeen"
    if num == 18:
        word = " Eighteen"
    if num == 19:
        word = " Nineteen"
    return word

def tens(num):
    if num == 20:
        word = " Twenty"
    if num == 30:
        word = " Thirty"
    if num == 40:
        word = " Fourty"
    if num == 50:
        word = " Fifty"
    if num == 60:
        word = " Sixty"
    if num == 70:
        word = " Seventy"
    if num == 80:
        word = " Eighty"
    if num == 90:
        word = " Ninety"
    return word


num = int(input("Enter number between 1-9999"))
word = ""

while num > 9999 or num < 0:
    print ("you've entered a null value please re-renter ")
    num = int(input("Enter number between 1-9999"))
if num >= 1000:
    word = ones(num//1000)+" thousand"
    num = num - ((num//1000) * 1000)
if num >= 100:
    word += ones(num//100) +" hundered"
    num = num - ((num//100) * 100)
if word != "" and num != 0:
    word = word + " and"
if num >= 20:
    word = word + tens(num // 10*10)
    num = num - (num // 10*10)
if num > 0 and num <= 19:
    word = word + ones(num)


print(word)
