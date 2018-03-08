name = input("Enter Name:")
salary = int(input("Enter your salary"))

print("------------------------------")
# if salary < 10000:
#     VAT = 0
# if salary >= 10000 and salary < 20000:
#     VAT = salary * 11 / 100
# if salary > 20000 and salary < 30000:
#     VAT = salary * 17/100
# if salary > 30000 and salary < 40000:
#     VAT = salary * 21/100
# else:
#     VAT = salary * 29/100

if salary < 10000:
    VAT = 0
elif salary >= 10000:
    VAT = salary * 11 / 100
elif salary > 20000:
    VAT = salary * 17 / 100
elif salary > 30000:
    VAT = salary * 21 / 100
elif salary >= 40000:
    VAT = salary * 29 / 100

print("VAT is:", VAT)
print("Net Salary is", (salary - VAT))
