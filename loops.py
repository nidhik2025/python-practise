#for
for i in range(5):
    print("hii" , i)

#"." inincreasing sequence
for number in range(5):
    print(number,(number + 1)*".")

#for else
Sucessful = False
for p in range(3):
    print("try again!")
    if Sucessful:
        print("sucessful")
        break
else:
    print("tried 3 times and failed")

#nested loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

#iterable string
for z in "mathematics":
    print(z)

#iterate string fro list
shopping_cart = ["apple","milk","flour","bread","curd"]
for item in shopping_cart:
    print(item)

#while loop
n = int(input("value of n : "))
while n > 0:
    print(n)
    n//=2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO",command)
#exercise
count = 0
for i in range(1,8):
    if i%2==0:
        print(i)
        count+=1
print(f"we have {count} even nummbrs")





