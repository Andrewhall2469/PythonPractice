product = input("Enter name of product")
quantity = int(input("Enter Quantity"))
unit_price = float(input("Enter Unit Price"))
choice = input("Is it a food item? Y or N")

if choice == "Y" or "y":
    VAT = 0
else:
    VAT = unit_price * quantity * 7 / 100

print("You bought:", quantity, product)
print("VAT Charged:", VAT)
