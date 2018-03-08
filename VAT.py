def VAT(salary):
    if salary > 20000:
        tax = salary * 21 / 100
    else:
        tax = salary * 17 / 100
    return tax

name = input("Enter Your Name")
salary = int(input("Enter Your Salary"))
print("---------------------------------------")
print("Your Salary:", salary)
print("VAT =", VAT(salary))
print("Net Salary =", salary-VAT(salary))