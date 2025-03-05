# exception is kind of error that terminates the program execution
numbers = [1,2]
print(numbers[3])

age = int(input("age:"))

# handling exeption
try:
    age = int(input("age:"))

except ValueError:
    print("you didn't enter valid age")

print("execution continuous")
