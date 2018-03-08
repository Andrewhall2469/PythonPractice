

name = input("Enter Name:")

phy = int(input("Enter Physics Marks"))
che = int(input("Enter Chemistry Marks"))
mat = int(input("Enter Maths Marks"))

TOT = phy + che + mat
per = TOT * 100 / 300
print("Total Marks:", TOT)
print("Percentage:", per)
print("------------------------")

if per >= 60:
    print("Mr", name, "You have passed!")

elif per < 60:
    print("Mr", name, "You have failed!")
