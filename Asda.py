bill = float(input("enter bill"))
amount_paid = float(input("enter amount paid"))
actBill = int(bill*100)
actPaid = int(amount_paid*100)
change = actPaid - actBill

print("Bill is: ", bill)
print("amount_paid is: ", amount_paid)

if change == 0:
    print("No change required")

if change >= 5000:
    n50 = change // 5000
    change = change - n50*5000
    print("£50 =", n50)
if change >= 2000:
    n20 = change // 2000
    change = change - n20*2000
    print("£20 =", n20)
if change >= 1000:
    n10 = change // 1000
    change = change - n10*10
    print("£10 =", n10)
if change >= 500:
    n5 = change // 500
    change = change - n5*500
    print("£5 =", n5)
if change >= 200:
    n2 = change // 200
    change = change - n2*200
    print("£2 =", n2)
if change >= 100:
    n1 = change // 100
    change = change - n1*100
    print("£1 =", n1)
if change >= 50:
    c50 = change // 50
    change = change - c50*50
    print("£0.50 =", c50)
if change >= 20:
    c20 = change // 20
    change = change - c20*20
    print("£0.20 =", c20)
if change >= 10:
    c10 = change // 10
    change = change - c10*10
    print("£0.10 =", c10)
if change >= 5:
    c5 = change // 5
    change = change - c5*5
    print("£0.05 =", c5)
if change >= 2:
    c2 = change // 2
    change = change - c2*2
    print("£0.02 =", c2)
if change >= 1:
    c1 = change // 1
    change = change - c1*1
    print("£0.01 =", c1)
