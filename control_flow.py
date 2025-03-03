#comparision
print(10>3)
print(10==3)
print(10!=3)

#conditional statement
temp = int(input("temp value : "))
if temp > 30 :
    print("its heat")

elif temp < 30:
    print("its cool")


#university info
age = int(input("age value:"))
message = "eligible" if age>=18 else "Not eligible" #ternary operator
print(message)

#logical operator
high_income = True
good_credit = False

if high_income and good_credit:
    print("you should have 2 year experiance")
else:
    print("you should have 4 year experience")

#chaining comparision operator
patientAge = int(input("enter petient age:"))
if 18<= patientAge<60:
    print("eligible for vacccination")
else:
    print("not eligible for vaccination")
#check if odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
